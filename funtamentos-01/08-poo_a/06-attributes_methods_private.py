class Person:
    
    def __init__(self, name, age):
        self.name = name # atributos de instancia
        self.age = age
        self.__password = "123" #name mangling
        # _Person_password
        
    def __generate__password(self):
        return f"$${self.name}{self.age}"
    
person1 = Person('david', 26)
print(person1.name)
# print(person1.__passworkd) error
print(person1.__Person__password) # do not do this but this is the way to get the info
print(person1.__Person__generate_password())