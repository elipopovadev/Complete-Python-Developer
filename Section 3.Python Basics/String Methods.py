name = 'elena'
print(name.capitalize())  # Elena

length = len(name)
print(length)  # 5

count_letter_e = name.count('e')
print(count_letter_e)  # 2

print(name.upper())  # ELENA

find_n = name.find('n')
print(find_n)  # 3

print(name.index('e'))  # 0

find_w = name.find('w')
print(find_w)  # -1 because 'w' doesn't exist

print(name.islower())  # True

# Check if the all string is letters or is digits
print(name.isalpha())  # True
print(name.isdigit())  # False

# Replace substring with another
print(name.replace('e', 'i')) # ilina
print(name) # name is the same: 'elena'

# Split string
new_string = name.split('e') 
print(new_string) # ['', 'l', 'na']
print(name) # name is the same: 'elena'

new_name = name * 3
print(new_name) # elenaelenaelena


