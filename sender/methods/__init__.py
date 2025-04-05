from .tcp import tcp
from .udp import udp
from sender.utils.logger import PacketLogger

_methods = {
    'tcp': tcp,
    'udp': udp
}

def get_method(method_name):
    """Получение метода по имени"""
    return _methods.get(method_name.lower())

def available_methods():
    """Список доступных методов"""
    return list(_methods.keys())

def register_method(name, method):
    """Регистрация нового метода"""
    if name.lower() in _methods:
        raise ValueError(f"Метод {name} уже зарегистрирован")
    _methods[name.lower()] = method
