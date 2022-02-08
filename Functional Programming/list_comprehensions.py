my_list = [char for char in "hello"]
print(my_list) # ['h', 'e', 'l', 'l', 'o']

my_list2 = [num for num in [1, 2, 3, 4, 5]]
print(my_list2) # [1, 2, 3, 4, 5]

my_list3 = [num * 2 for num in [1, 2, 3, 4, 5]]
print(my_list3) # [2, 4, 6, 8, 10]

my_list4 = [num for num in range(0, 100) if num % 2 == 0]
print(my_list4) 

my_list5 = [num * 2 for num in range(0, 100) if num % 2 != 0]
print(my_list5)
