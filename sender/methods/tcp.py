from sender.utils.network import create_tcp_socket
from sender.methods.base_method import BaseMethod

class TCPMethod(BaseMethod):
    def send_packet(self):
        sock = create_tcp_socket(self.target_ip, self.target_port)
        if sock:
            try:
                sock.send(b'X' * 1024)  # Отправляем 1KB данных
            except:
                pass
            finally:
                sock.close()

def tcp(target_ip, target_port, duration):
    return TCPMethod(target_ip, target_port, duration)
