import time
from sender.utils.logger import PacketLogger

class BaseMethod:
    """Базовый класс для всех методов атаки"""
    
    def __init__(self, target_ip, target_port, duration, settings, logger: PacketLogger):
        self.target_ip = target_ip
        self.target_port = target_port
        self.duration = duration
        self.settings = settings
        self.logger = logger
        self.running = False
        self.packets_sent = 0
    
    def attack(self):
        """Основной метод запуска атаки"""
        self.running = True
        start_time = time.time()
        
        self.logger.log_info(f"Начало {self.__class__.__name__} атаки")
        
        try:
            while self.running and time.time() - start_time < self.duration:
                self.send_packet()
                self.packets_sent += 1
                
                # Логирование прогресса каждые 5 секунд
                if int(time.time() - start_time) % 5 == 0:
                    self.logger.log_debug(f"Отправлено пакетов: {self.packets_sent}")
                    
        except Exception as e:
            self.logger.log_error(f"Ошибка во время атаки: {str(e)}")
            raise
        finally:
            self.cleanup()
            self.logger.log_info(f"Атака завершена. Всего отправлено пакетов: {self.packets_sent}")
    
    def send_packet(self):
        """Метод отправки пакета (должен быть реализован в подклассах)"""
        raise NotImplementedError("Подклассы должны реализовать этот метод")
    
    def cleanup(self):
        """Очистка ресурсов после атаки"""
        pass
