from abc import ABC, abstractmethod

# clase abstracta
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass
    
    def sleep(self):
        print('zzzz....')

class Dog(Animal):
    def sound(self):
        return print('guau guau')

class Cat(Animal):
    def sound(self):
        return print('meow!')

taquito = Dog()
misifus = Cat()

misifus.sound()