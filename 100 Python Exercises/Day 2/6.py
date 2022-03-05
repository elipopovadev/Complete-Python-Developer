import math

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

