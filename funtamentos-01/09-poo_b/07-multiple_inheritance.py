class Flyer:
    def fly(self):
        print("puedo volar")
        
class Swimmer:
    def swing(self):
        print("puedo nadar")
    
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")
        
donald = Duck()
donald.fly()
donald.swing()
donald.quack()

# MRO method resolution order
print(Duck.__mro__)