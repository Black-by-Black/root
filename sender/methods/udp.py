import random
from sender.utils.network import create_udp_socket
from sender.methods.base_method import BaseMethod

class UDPMethod(BaseMethod):
    def send_packet(self):
        sock = create_udp_socket()
        try:
            # Генерируем случайные данные для отправки
            data = bytes([random.randint(0, 255) for _ in range(1024)])
            sock.sendto(data, (self.target_ip, self.target_port))
        except:
            pass
        finally:
            sock.close()

def udp(target_ip, target_port, duration):
    return UDPMethod(target_ip, target_port, duration)
