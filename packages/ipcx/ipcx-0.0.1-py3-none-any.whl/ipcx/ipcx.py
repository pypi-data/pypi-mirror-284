from ipcx.src.server import Server
from ipcx.src.client import Client
from ipcx.src.globals import Globals

from types import FunctionType

def share(*_, **__):
    def decorator(func):
        if func.__class__ != FunctionType:

            for f in dir(func):
                if not f.startswith("__"):
                    Globals.shared_functions[f] = getattr(func, f)
        
        else:
            Globals.shared_functions[func.__name__] = func
        
        return func
    return decorator

def port_range(port):
    if port <= Globals.port_range:
        port = Globals.port_start + port
    return port

def serv(port):
    port = port_range(port)

    server = Server("127.0.0.1", port)

    if not server.try_bind():
        raise Exception(f"Cannot bind the server to 127.0.0.1:{port}")
    
    server.start()

    return server

def connect(port):
    port = port_range(port)

    client = Client("127.0.0.1", port)
    client.start()

    return client

def init_master(master_class, port):
    port = port_range(port)

    server = Server("127.0.0.1", port)

    if server.try_bind():
        share()(master_class)
        server.start()
        return master_class
    else:
        client = Client("127.0.0.1", port)
        client.start()
        return client
    
