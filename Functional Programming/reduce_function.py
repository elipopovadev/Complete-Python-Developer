from functools import reduce

def accumulator(acc, element):
    return acc + element

my_list = [1, 2, 3, 4]

print(reduce(accumulator, my_list, 0)) # 10
