basket = ['a', 'b', 'b', 'c', 'd', 'e']

new_basket = basket[::-1]
print(new_basket)  # ['e', 'd', 'c', 'b', 'b', 'a']
print(basket)  # ['a', 'b', 'b', 'c', 'd', 'e']

basket.reverse()
print(basket)  # ['e', 'd', 'c', 'b', 'b', 'a']

print(' '.join(basket))  # e d c b b a
print('!'.join(basket))  # e!d!c!b!b!a

my_list = list(range(0, 101))
list_str = map(str, my_list)
print(' '.join(list_str))
