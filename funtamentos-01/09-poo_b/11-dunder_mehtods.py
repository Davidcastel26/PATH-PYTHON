# dunder
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"hola soy {self.name}"
    
    def __len__(self):
        return len(self.name)
    
eu = Person("David")
print(eu)
print(len(eu))