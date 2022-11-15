class Pet:
    def __init__ (self,name,species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} is a {self.species}"
    
class Dog(Pet):
    