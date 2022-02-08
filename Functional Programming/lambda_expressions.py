from functools import reduce


my_list = [1, 2, 3, 4, 5]

print(list(map(lambda x: x * 2, my_list))) # [2, 4, 6, 8, 10]

print(list(filter(lambda x: x % 2 == 0, my_list))) # [2, 4]

print(reduce(lambda acc, element: acc + element, my_list, 0)) # 15
