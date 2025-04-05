import socket

def create_tcp_socket(target_ip, target_port, settings):
    """Создание TCP сокета"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(settings.socket_timeout)
    try:
        sock.connect((target_ip, target_port))
        return sock
    except socket.error as e:
        if settings.verbose:
            print(f"Ошибка подключения TCP: {e}")
        return None

def create_udp_socket(settings):
    """Создание UDP сокета"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(settings.socket_timeout)
    return sock
