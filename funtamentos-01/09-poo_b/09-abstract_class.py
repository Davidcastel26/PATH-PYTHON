from abc import ABC, abstractmethod

# clase abstracta
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass
    
    def sleep(self):
        print('zzzz....')

