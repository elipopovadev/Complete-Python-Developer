first_set = {1, 2, 3, 4, 5, 6}
second_set = {2, 6, 7, 5, 10}

print(first_set.union((second_set)))  # {1, 2, 3, 4, 5, 6, 7, 10}
print(first_set)  # {1, 2, 3, 4, 5, 6}

print(first_set.intersection((second_set)))  # {2, 5, 6}
print(first_set)  # {1, 2, 3, 4, 5, 6}

print(first_set.difference(second_set))  # {1, 3, 4}
print(second_set.difference((first_set)))  # {10, 7}

print(first_set.isdisjoint({1000, 3000}))  # True
print(first_set)  # {1, 2, 3, 4, 5, 6}

print(first_set.issubset(second_set))  # False
print(first_set.issuperset(second_set))  # False
