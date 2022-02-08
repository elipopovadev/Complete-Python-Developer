my_list = [1, 2, 3, 4, 5]

my_set1 = {num for num in my_list} # {1, 2, 3, 4, 5}
print(my_set1)

my_set2 = {num * 2 for num in my_list} 
print(my_set2) # {2, 4, 6, 8, 10}

my_set3 = {num for num in my_list if num % 2 == 0} 
print(my_set3) # {2, 4}

my_set4 = {num * 2 for num in my_list if num % 2 != 0}
print(my_set4) # {2, 10, 6}