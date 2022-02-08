from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def func_capitalize(element):
    return element.capitalize()

new_list = list(map(func_capitalize, my_pets))
print(new_list) # ['Sisi', 'Bibi', 'Titi', 'Carla']


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

sorted_numbers = sorted(my_numbers)
new_zip_list = list(zip(my_strings, sorted_numbers))
print(new_zip_list) # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def filter_over_fifthy(element):
    return element > 50

filtered_list = list(filter(filter_over_fifthy, scores))
print(filtered_list) # [73, 65, 76, 100, 88]

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, element):
    return acc + element

mix_list = my_numbers + scores
print(mix_list) 
print(reduce(accumulator, mix_list, 0)) # 456
