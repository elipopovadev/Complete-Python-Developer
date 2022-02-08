simple_dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

new_dict1 = {key : value * 2 for key, value in simple_dict.items()}
print(new_dict1) # {'a': 2, 'b': 4, 'c': 6}

new_dict2 = {key : value * 2 for key, value in simple_dict.items() if value % 2 == 0}
print(new_dict2) # {'b': 4}

new_dict3 = {num : num * 2 for num in [1, 2, 3, 4]}
print(new_dict3) # {1: 2, 2: 4, 3: 6, 4: 8}
