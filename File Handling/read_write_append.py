my_file = open('test.txt', mode = 'w')
my_file.write('Hello!')
my_file.close()

my_file = open('test.txt', mode = 'a')
my_file.write(" My name is Elena!")
my_file.write(" How are you?")
my_file.close()

try:
  my_file = open('test.txt', mode = 'r')
  for line in my_file:
     print(line)
  my_file.close()
except FileNotFoundError as error:
    raise error
