my_dictionary = {
    'a': [1, 2, 3],
    'b': 5,
    'c': True
}

print(my_dictionary['a'])  # [1, 2, 3]
print(my_dictionary['a'][0])  # 1
print(my_dictionary['c'])  # True

my_list = [
    {
        'a': [1, 2, 5],
        'b': True
    },
    {

        'a': [1, 2, 3],
        'b': 5,
    }
]

print(my_list[0]) # {'a': [1, 2, 5], 'b': True}
print(my_list[0]['a'][1]) # 2