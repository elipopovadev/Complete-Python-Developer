my_tuple = (1, 2, 2, 3, 4, 5)  # immutable collection
print(my_tuple.index(5)) # 5
print(my_tuple.count(2)) # 2
print(len(my_tuple)) # 6
print(my_tuple) # (1, 2, 2, 3, 4, 5)

new_tuple = my_tuple[::-1]
print(new_tuple) # (5, 4, 3, 2, 2, 1)

user = {
    (1,2): [1,2,3],
    'town': 'Varna',
    'age': 99
}

user.update({(1,2): 100})
print(user.items()) # dict_items([((1, 2), 100), ('town', 'Varna'), ('age', 99)]) # printed like tuple
print(user) # {(1, 2): 100, 'town': 'Varna', 'age': 99}
