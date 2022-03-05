# Write a program that accepts sequence of lines as input and prints the lines after making all characters
# in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

text_array = []
while True:
    text = input().upper()
    if text:
       text_array.append(text)
    else:
        break

for line in text_array:
    print(line)
    
