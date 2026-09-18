class Flyer:
    def fly(self):
        print("puedo volar")
    
    def do_something(self):
        print("Hago algo en la clase Flyer")
        
class Swimmer:
    def swing(self):
        print("puedo nadar")
    
class Duck():
    
    def __init__(self):
        self.flyer = Flyer()
        self.swimmer = Swimmer()
    
    def quack(self):
        print("Quack!")
        
    def start_fly(self):
        self.flyer.fly()
        
    def start_swimg(self):
        self.swimmer.swing()
        
donald = Duck()
donald.start_fly()
donald.start_swimg()
donald.quack()

# MRO method resolution order
print(Duck.__mro__)