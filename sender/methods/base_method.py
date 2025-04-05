import time

class BaseMethod:
    """Базовый класс для всех методов атаки"""
    
    def __init__(self, target_ip, target_port, duration, settings):
        self.target_ip = target_ip
        self.target_port = target_port
        self.duration = duration
        self.settings = settings
        self.running = False
    
    def attack(self):
        """Основной метод запуска атаки"""
        self.running = True
        start_time = time.time()
        
        if self.settings.verbose:
            print(f"Атака начата на {self.target_ip}:{self.target_port}")
        
        while self.running and time.time() - start_time < self.duration:
            self.send_packet()
        
        self.cleanup()
        
        if self.settings.verbose:
            print("Атака завершена")
    
    def send_packet(self):
        """Метод отправки пакета (должен быть реализован в подклассах)"""
        raise NotImplementedError("Подклассы должны реализовать этот метод")
    
    def cleanup(self):
        """Очистка ресурсов после атаки"""
        pass
