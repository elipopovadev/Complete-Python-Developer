def only_even(element):  
    return element % 2 == 0

my_list = [1, 2, 3, 4, 5]

print(list(filter(only_even, my_list))) # [2, 4]
print(my_list) # [1, 2, 3, 4, 5]
