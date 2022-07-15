from .abs_auto import AbsAuto

class Jeep(AbsAuto):
    def start(self):
        print('jeep running very slow at start')
        
    def stop(self):
        print('jeep is stoping here')