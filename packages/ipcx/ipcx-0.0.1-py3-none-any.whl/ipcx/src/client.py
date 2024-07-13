import threading
import socket
import json

from ipcx.src.types import TypeDeserializer

class Client():

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.request_lock = threading.Lock()
    
    def function(self, name):
        def wrapper(*args, **kwargs):
            return self.request(name, *args, **kwargs)
        return wrapper

    def start(self):
        self.sock.connect((self.host, self.port))
        self.functions = self.recv_json()
        
        for f in self.functions:
            setattr(self, f, self.function(f))
        
    def send_json(self, data):
        self.sock.sendall(json.dumps(data).encode())
    
    def recv_json(self):
        return json.loads(self.sock.recv(4096).decode())
    
    def request(self, function, *args, **kwargs):
        self.request_lock.acquire()

        self.send_json({
            "function": function,
            "args": args,
            "kwargs": kwargs
        })
        data = self.recv_json()

        self.request_lock.release()

        return TypeDeserializer(data["return"]["type"], data["return"]["value"]).deserialize()