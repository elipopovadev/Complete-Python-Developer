some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
some_dictionary = {}

for element in some_list:
    if not element in some_dictionary:
       some_dictionary[element] = 1
    else:
        some_dictionary[element] += 1

for key, value in some_dictionary.items():
    if value > 1:
       print(key, end = ' ')
