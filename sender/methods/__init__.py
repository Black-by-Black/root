from .tcp import tcp
from .udp import udp

_methods = {
    'tcp': tcp,
    'udp': udp
}

def get_method(method_name):
    return _methods.get(method_name.lower())

def available_methods():
    return list(_methods.keys())

def register_method(name, method):
    _methods[name.lower()] = method
