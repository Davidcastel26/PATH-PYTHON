class Person:
    
    def __init__(self, name):
        self.name = name # atributos de instancia
        self._energy = 100
        
    def _waste_energy(self, quantity):
        self._energy -= quantity