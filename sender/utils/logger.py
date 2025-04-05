import logging
from datetime import datetime
from sender.settings.config import Settings

class PacketLogger:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.setup_logging()
        
    def setup_logging(self):
        """Настройка системы логирования"""
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger('PacketSender')
        
        # Формат логов
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        # Логгер для ошибок
        error_handler = logging.FileHandler('errors.log')
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(formatter)
        
        # Логгер общей информации
        info_handler = logging.FileHandler('logs.log')
        info_handler.setLevel(logging.INFO)
        info_handler.setFormatter(formatter)
        
        # Логгер отладки
        debug_handler = logging.FileHandler('debug.log')
        debug_handler.setLevel(logging.DEBUG)
        debug_handler.setFormatter(formatter)
        
        # Добавляем обработчики
        self.logger.addHandler(error_handler)
        self.logger.addHandler(info_handler)
        self.logger.addHandler(debug_handler)
        
    def log_error(self, message):
        """Логирование ошибок"""
        self.logger.error(message)
        
    def log_info(self, message):
        """Логирование информации"""
        self.logger.info(message)
        
    def log_debug(self, message):
        """Логирование отладочной информации"""
        if self.settings.debug:
            self.logger.debug(message)
