
class Animal:
    
    def __init__(self, name):
        self.name = name
        
    def sleep(self):
        print(f"{self.name} esta durmiendo")
    
class Dog(Animal):
    def dog_sound(self):
        print(f"{self.name} dice: guau!")

class Cat(Animal):
    def cat_sound(self):
            print(f"{self.name} dice: guau!")
        
firulais = Dog('Firulis')
firulais.sleep()
firulais.dog_sound()