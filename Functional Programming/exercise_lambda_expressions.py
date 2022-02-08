#Square
my_list = [5, 4, 3]
print(list(map(lambda x: x**2, my_list))) # [25, 16, 9]

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(a, key = lambda x: x[1])) # [(10, -1), (0, 2), (4, 3), (9, 9)]
