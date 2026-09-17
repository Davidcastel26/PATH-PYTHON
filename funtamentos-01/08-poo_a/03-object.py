
class Person:
    def __init__(self, name, age):
        if(age > 18): 
            self.name = name
            self.age = age
    
person1 = Person('david',26)

print(person1)
print(person1.name)