def func_multiply_by2(list):
    result = []
    for element in list:
        new_element = element * 2
        result.append(new_element)
    return result
     
        
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(func_multiply_by2(my_list))
