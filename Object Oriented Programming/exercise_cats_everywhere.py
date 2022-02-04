#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Misho", 2)
cat2 = Cat("Milko", 4)
cat3 = Cat("Elmo", 8)



# 2 Create a function that finds the oldest cat
def find_the_oldest_cat(*cats):
    return max(cats, key = lambda cat: cat.age)



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest_cat = find_the_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, {oldest_cat.age} years old")
