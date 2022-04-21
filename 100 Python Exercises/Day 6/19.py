'''
Question 19:

    You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string,
    age and score are numbers. The tuples are input by console. The sort criteria is:

    1: Sort based on name
    2: Then sort based on age
    3: Then sort by score

    The priority is that name > age > score.

    If the following tuples are given as input to the program: '''

information = []
while True:
    line = input().split(',')
    if line == ['Stop']:
        break
    name = line[0]
    age = int(line[1])
    score = int(line[2])
    information.append((name, age, score))

sorted_information = sorted(
    information, key=lambda tup: (tup[0], tup[1], tup[2]))
string_tuple = [tuple(map(str, tup)) for tup in sorted_information]
print(string_tuple)
