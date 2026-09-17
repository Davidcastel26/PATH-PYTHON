class Person:
    species = "Human"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species
        # changes a class level not changes in general level
        