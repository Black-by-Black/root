import re
from sender.methods import available_methods
from sender.settings.constants import *

def validate_ip(ip):
    """Проверка корректности IP адреса"""
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return False
    return all(0 <= int(num) <= 255 for num in ip.split('.'))

def validate_port(port, settings):
    """Проверка корректности порта"""
    return settings.min_port <= port <= settings.max_port

def validate_method(method):
    """Проверка доступности метода"""
    return method in available_methods()

def validate_time(time, settings):
    """Проверка допустимого времени атаки"""
    return 0 < time <= settings.max_attack_duration

def validate_input(ip, port, method, time, settings):
    """Комплексная проверка всех входных данных"""
    if not validate_ip(ip):
        print("Ошибка: некорректный IP адрес")
        return False
    if not validate_port(port, settings):
        print(f"Ошибка: порт должен быть в диапазоне {settings.min_port}-{settings.max_port}")
        return False
    if not validate_method(method):
        print(f"Ошибка: неизвестный метод. Доступные: {', '.join(available_methods())}")
        return False
    if not validate_time(time, settings):
        print(f"Ошибка: время должно быть от 1 до {settings.max_attack_duration} секунд")
        return False
    return True
