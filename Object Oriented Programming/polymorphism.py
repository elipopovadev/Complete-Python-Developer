class Cat():
    def __init__(self, name, age):
         self.name = name
         self.age = age
         
    def eat(self):
        print("Cat is eating...")
        

class PersianCat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)

class BengalCat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
        

class SiberianCat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)


cat1 = PersianCat("Eli", 3)
print(cat1.name)
cat1.eat()
cat2 = SiberianCat("Mimi", 2)
print(cat2.name)
cat2.eat()
