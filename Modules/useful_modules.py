from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 4, 3, 4, 4, 5, 6, 6, 7, 8]
print(Counter(li)) # Counter({4: 3, 6: 2, 1: 1, 2: 1, 3: 1, 5: 1, 7: 1, 8: 1})

dict = defaultdict(int, {'a': 1, 'b': 2, 'c': 4})
print(dict['d']) # 0

dict2 = defaultdict(lambda: "value does not exist", {'a': 1, 'b': 2})
print(dict2['d']) # value does not exist

dict3 = OrderedDict()
products = {"3" : "banana", "1" : "apple", "5" : "potatoes"}
for key, value in products.items():
    dict3[key] = value
    
print(dict3)

