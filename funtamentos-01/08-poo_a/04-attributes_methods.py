

class Person:
    
    species = "Humano"
    
    def __init__(self, name, age):
        self.name = name #atributos de instacia
        self.age = age
    
    def work(self):
        return f"{self.name} is working"
    
    def eat(self, food):
        if food.lower() == 'tacos':
            return "gordito"
        else:
            return "+Energy"
    
# objeto
parson1 = Person('Ricardo', 29)

print(parson1.name)
print(parson1.age)
print(parson1.species)
print(parson1.work())