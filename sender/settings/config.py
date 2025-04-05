from .constants import *

class Settings:
    def __init__(self):
        # Настройки сети
        self.packet_size = DEFAULT_PACKET_SIZE
        self.socket_timeout = DEFAULT_TIMEOUT
        
        # Ограничения
        self.max_port = MAX_PORT
        self.min_port = MIN_PORT
        self.max_attack_duration = MAX_ATTACK_DURATION
        
        # Дополнительные параметры
        self.verbose = False  # Режим подробного вывода
        
    def update(self, **kwargs):
        """Обновление настроек"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
