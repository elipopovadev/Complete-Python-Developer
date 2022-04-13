import numpy as np
'''Question 12:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit
of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.'''

sample_list = []
sample_array = range(1000, 3001)
for variable in sample_array:
    var = str(variable)
    if int(var[0]) % 2 == 0 and int(var[1]) % 2 == 0 and int(var[2]) % 2 and int(var[3]) % 2 == 0:
        sample_list.append(var)

print(",".join(sample_list))
