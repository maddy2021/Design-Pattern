from abc import ABC,abstractmethod

class AbsAuto(ABC):
    @abstractmethod
    def start():
        pass

    @abstractmethod
    def stop():
        pass