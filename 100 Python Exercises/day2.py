import math

# 4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
# which contains every number.Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

numbers = input()
numbers = numbers.split(',')
list = []

for num in numbers:
    list.append(num) 

my_tuple = tuple(list)

print(list)
print(my_tuple)
    

# 5. Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class MyClass():
    def __init__(self, input):
        self.input = input
    
    def getString(self):
        return str(self.input)
           
    def printString(self):
        result = self.getString()
        print(result.upper())
        

def test(input):
    my_class = MyClass(input)
    string = my_class.getString()
    print(string)
    my_class.printString()
    

test_input = input()
test(test_input)


# 6. Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

def function(input):
    numbers = input
    li = numbers.split(',')
    C, H = 50, 30
    result = []
    for num in li:
        Q = round(math.sqrt((2 * C * float(num)) / H ))
        result.append(str(Q))
    return(",".join(result))

text = input()
print(function(text))


# 7. _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i _ j.*
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

x = int(input())
y = int(input())

row = x
col = y

array = [[0] * col for r in range(row)]

for r in range(len(array)):
    for c in range(len(array[r])):
        array[r][c] = r * c

print(array)
