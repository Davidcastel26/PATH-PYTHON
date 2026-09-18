class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sound(self):
        print(f"{self.name} hace un sonido")
    
    def info(self):
        print(f"Soy {self.name} y tengo {self.age}")
        
class Dog(Animal):
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def sound(self):
        super().sound()
        print(f"{self.name} dice: guau!")
        
firulais = Dog('Firulais', 5, 'Lab')
firulais.sound()