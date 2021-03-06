user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

user2 = {
    'basket': [10, 20, 30],
    'greet': 'hello',
    'age': 30
}

print(user['basket'])
print(user2['basket'])
print(user.get('name'))  # None
print(user.get('name', 'Elena'))  # default = 'Elena'; print: Elena
checker = 'basket' in user2.keys()
print(checker)  # True
print(30 in user2.values())  # True
# dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)])
print(user.items())

user3 = user2  # user3 points in the same ref like user2
user3.clear()
print(user3)  # {}
print(user2)  # {}

user4 = user.copy()
user4.clear()
print(user4)  # {}
print(user)  # {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
print(user.pop('age'))  # 20
print(user)  # {'basket': [1, 2, 3], 'greet': 'hello'}
user.popitem()
print(user)  # {'basket': [1, 2, 3]}

user.update({'age': 90})
print(user)  # {'basket': [1, 2, 3], 'age': 90}
user.update({'name': 'Elena'})
print(user)  # {'basket': [1, 2, 3], 'age': 90, 'name': 'Elena'}
