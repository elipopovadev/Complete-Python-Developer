my_set = {1,2,3,4,5}
my_set.add(10)
my_set.add(10)
print(my_set) # {1, 2, 3, 4, 5, 10}

my_set.pop()
print(my_set) # {2, 3, 4, 5, 10}; the first element is removed

my_set.remove(4)
print(my_set) # {2, 3, 5, 10}

my_set.pop() 
print(my_set) # {3, 5, 10}; the first element is removed

my_list = [10,20,30,40,50]
my_list.pop()
print(my_list) # [10, 20, 30, 40]; the last element is removed
print(my_list[::-1]); # reversed order: [40, 30, 20, 10]

#Delete last element of set 
print(my_set) # {3, 5, 10}
my_list2 = list(my_set)
my_list2.pop()
my_set = set(my_list2) 
print(set(my_set)) # {3, 5}
print(10 in my_set) # False
