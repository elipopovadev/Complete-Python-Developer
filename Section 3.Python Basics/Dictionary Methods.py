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
print(user.get('name')) # None
print(user.get('name', 'Elena')) # default = 'Elena'; print: Elena
