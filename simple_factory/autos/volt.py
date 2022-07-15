from .abs_auto import AbsAuto

class Volt(AbsAuto):
    def start(self):
        print('volt running very fast like lightning')
        
    def stop(self):
        print('volt is stoping here')