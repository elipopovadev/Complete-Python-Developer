import random 

my_list = ["apple", "orange", "tomato", "potatoes"]
print(random.choice(my_list))

numbers = [20, 40, 50, 30]
random.shuffle(numbers)
print(numbers)

print(random.randint(0, len(numbers)))
