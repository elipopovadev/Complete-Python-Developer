class Cat:
    species = "mammal"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eating(self): # Instance method
        return (f" {self.name} is eating...")
     
    @classmethod   
    def get_species(cls):
        return cls.species
    
    @staticmethod
    def info():
        print("This is class Cat")
    
    
cat1 = Cat("Robi", 5)
print(cat1.eating()) # Instance method

print(Cat.get_species()) # Classmethod method
    
Cat.info() # Static method