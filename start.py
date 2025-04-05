import argparse
from sender.methods import get_method
from sender.utils.validator import validate_input

def main():
    parser = argparse.ArgumentParser(description='Packet sender tool')
    parser.add_argument('--ip', required=True, help='Target IP address')
    parser.add_argument('--port', required=True, type=int, help='Target port')
    parser.add_argument('--method', required=True, help='Attack method (tcp, udp, etc.)')
    parser.add_argument('--time', required=True, type=int, help='Duration in seconds')
    
    args = parser.parse_args()
    
    if not validate_input(args.ip, args.port, args.method, args.time):
        return
    
    method = get_method(args.method)
    if method:
        method(args.ip, args.port, args.time).attack()
    else:
        print(f"Unknown method: {args.method}")

if __name__ == "__main__":
    main()
