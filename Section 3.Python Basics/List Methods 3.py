basket = ['a', 'b', 'x', 'c', 'd', 'e']
basket.sort()
print(basket)  # ['a', 'b', 'c', 'd', 'e', 'x']

new_basket = ['f', 'g', 'a', 'b']
print(sorted(new_basket))  # ['a', 'b', 'f', 'g']
print(new_basket)  # ['f', 'g', 'a', 'b']

basket.reverse()
print(basket)  # ['x', 'e', 'd', 'c', 'b', 'a']
