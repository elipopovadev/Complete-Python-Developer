''' Question 14:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9 '''

input_ = input()
upper_case = []
lower_case = []
for element in input_:
    if element.islower():
        lower_case.append(element)
    elif element.isupper():
        upper_case.append(element)
print(f"UPPER CASE {len(upper_case)}")
print(f"LOWER CASE {len(lower_case)}")
