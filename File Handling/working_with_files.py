my_file = open('test.txt')
for line in my_file:
   print(line)

# print(my_file.read)
# print(my_file.readlines()) # ['Hi, my name is Elena Popova!\n', ':)\n', 'How are you?']
my_file.close()
