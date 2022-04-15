'''Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''

input_ = input()
digits = []
letters = []

for element in input_:
    if element.isalpha():
        letters.append(element)
    elif element.isdigit():
        digits.append(element)

print(f"Letters {len(letters)}")
print(f"Digits {len(digits)}")
