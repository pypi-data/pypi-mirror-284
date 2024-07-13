import socket
import threading
import json

from ipcx.src.globals import Globals
from ipcx.src.types import TypeSerializer

class Connection(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def send_json(self, data):
        self.conn.sendall(json.dumps(data).encode())

    def recv_json(self):
        data = self.conn.recv(4096).decode()
        if data == "":
            raise Exception("Connection closed")
        return json.loads(data)
    
    def request(self, function, args, kwargs):
        return Globals.shared_functions[function](*args, **kwargs)

    def run(self):
        self.send_json(list(Globals.shared_functions.keys()))

        try:
            while True:
                data = self.recv_json()
                return_value = self.request(data["function"], data["args"], data["kwargs"])
                self.send_json({
                    "return": TypeSerializer(return_value).serialize()
                })
        except: pass
        finally:
            self.conn.close()

class Server(threading.Thread):

    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def try_bind(self):
        try:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind((self.host, self.port))
            return True
        except:
            self.close()
            return False
    
    def close(self):
        self.sock.close()

    def run(self):
        self.sock.listen()

        try:
            while True:
                Connection(*self.sock.accept()).start()
        except: pass
        finally:
            self.sock.close()
        