
class Animal:
    def make_sound(self):
        print("sonido de animal")

class Dog(Animal):
    def make_sound(self):
        print("woof woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow Meow!")
        
def make_noise(animal):
    if isinstance(animal, Animal):
        animal.make_sound()
    else:
        print("El objeto no es un Animal")
        
make_noise(Dog())
make_noise(Cat())
make_noise('Perro')