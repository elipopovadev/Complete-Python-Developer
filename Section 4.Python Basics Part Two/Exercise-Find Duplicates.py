some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
some_dictionary = {}

for element in some_list:
    if element not in some_dictionary:
       some_dictionary[element] = 1
    else:
        some_dictionary[element] += 1

for key, value in some_dictionary.items():
    if value > 1:
       print(key, end = ' ')

# another way
duplicates = []

for x in some_list:
    if some_list.count(x) > 1 and x not in duplicates:
       duplicates.append(x)
        
print()
print(duplicates)