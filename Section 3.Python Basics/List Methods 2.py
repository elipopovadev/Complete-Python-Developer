basket = ['a', 'b', 'b', 'c', 'd', 'e']

print(basket.index('c')) # 3
print(basket.index('b', 2)) # 2
print('e' in basket) # True
print('z' in basket) # False
print(basket.count('b')) # 2
print(basket.count('d')) # 1