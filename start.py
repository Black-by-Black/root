import argparse
from sender.methods import get_method
from sender.utils.validator import validate_input
from sender.settings.config import Settings
from sender.utils.logger import PacketLogger

def main():
    # Инициализация настроек
    settings = Settings()
    logger = PacketLogger(settings)
    
    try:
        # Настройки парсера аргументов командной строки
        parser = argparse.ArgumentParser(description='Утилита для отправки сетевых пакетов')
        parser.add_argument('--ip', required=True, help='Целевой IP адрес')
        parser.add_argument('--port', required=True, type=int, help='Целевой порт')
        parser.add_argument('--method', required=True, help='Метод атаки (tcp, udp и др.)')
        parser.add_argument('--time', required=True, type=int, help='Длительность в секундах')
        parser.add_argument('--debug', action='store_true', help='Режим отладки')
        
        args = parser.parse_args()
        
        # Обновляем настройки
        if args.debug:
            settings.debug = True
            settings.verbose = True
        
        # Валидация входных данных
        if not validate_input(args.ip, args.port, args.method, args.time, settings):
            logger.log_error(f"Невалидные входные данные: {args}")
            return
        
        # Логирование начала атаки
        logger.log_info(f"Запуск атаки: {args.method} на {args.ip}:{args.port} в течение {args.time} сек.")
        
        # Получение и запуск метода
        method = get_method(args.method)
        if method:
            method(args.ip, args.port, args.time, settings, logger).attack()
        else:
            error_msg = f"Неизвестный метод: {args.method}"
            logger.log_error(error_msg)
            print(error_msg)
            
    except Exception as e:
        logger.log_error(f"Критическая ошибка: {str(e)}")
        print(f"Произошла ошибка: {str(e)}. Подробности в логах.")
    finally:
        logger.log_info("Работа программы завершена")

if __name__ == "__main__":
    main()
