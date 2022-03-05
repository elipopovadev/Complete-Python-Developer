# 2. Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

num = int(input()) 
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print(fact)

