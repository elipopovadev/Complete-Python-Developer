for i, char in enumerate('Elena Popova'):
    print(f'{i} : {char}')

for i, item in enumerate([1, 2, 3, 4, 5]):
    print(f'{i} : {item}')

for i, item in enumerate({1, 2, 3, 4, 5}):
    print(f'{i} : {item}')

for i, item in enumerate((10, 20, 39, 40, 54)):
    print(f'{i} : {item}')

for i, item in enumerate({'name': 'Elena', 'age': 100}):
    print(f'{i} : {item}')  # 0 : name 1 : age
