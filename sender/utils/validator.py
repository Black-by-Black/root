import re
from sender.methods import available_methods

def validate_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return False
    return all(0 <= int(num) <= 255 for num in ip.split('.'))

def validate_port(port):
    return 1 <= port <= 65535

def validate_method(method):
    return method in available_methods()

def validate_time(time):
    return time > 0

def validate_input(ip, port, method, time):
    if not validate_ip(ip):
        print("Invalid IP address")
        return False
    if not validate_port(port):
        print("Invalid port number (1-65535)")
        return False
    if not validate_method(method):
        print(f"Invalid method. Available: {', '.join(available_methods())}")
        return False
    if not validate_time(time):
        print("Time must be positive integer")
        return False
    return True
