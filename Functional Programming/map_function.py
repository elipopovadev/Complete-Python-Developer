def func_multiply_by2(element):  
    return element * 2

my_list = [1, 2, 3, 4, 5]

print(list(map(func_multiply_by2, my_list))) # [2, 4, 6, 8, 10]
print(my_list) # [1, 2, 3, 4, 5]
