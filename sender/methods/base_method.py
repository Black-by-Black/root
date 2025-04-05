import time

class BaseMethod:
    def __init__(self, target_ip, target_port, duration):
        self.target_ip = target_ip
        self.target_port = target_port
        self.duration = duration
        self.running = False
    
    def attack(self):
        self.running = True
        start_time = time.time()
        
        while self.running and time.time() - start_time < self.duration:
            self.send_packet()
        
        self.cleanup()
    
    def send_packet(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def cleanup(self):
        pass
