'''
Question 18:
    A website requires the users to input username and password to register.
    Write a program to check the validity of password input by users.

    Following are the criteria for checking the password:

    At least 1 letter between [a-z]
    At least 1 number between [0-9]
    At least 1 letter between [A-Z]
    At least 1 character from [$#@]
    Minimum length of transaction password: 6
    Maximum length of transaction password: 12

    Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
    Passwords that match the criteria are to be printed, each separated by a comma.

    Example

    If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345

    Then, the output of the program should be:

ABd1234@1 '''

input_array = input().split(",")


def password_checker(password):
    string_pass = str(password)
    digits = 0
    lower_letters = 0
    upper_letters = 0
    symbols_array = ['$', '#', '@']
    symbols = 0
    if len(string_pass) < 6 or len(string_pass) > 12:
        return False
    for element in string_pass:
        if element.isalpha() and element.islower():
            lower_letters += 1
        elif element.isalpha():
            upper_letters += 1
        elif element.isdigit():
            digits += 1
        elif element in symbols_array:
            symbols += 1
        else:
            return False
    if digits < 1 or lower_letters < 1 or upper_letters < 1 or symbols < 1:
        return False

    return True


valid_pass = []
for password in input_array:
    checker = password_checker(password)
    if checker:
        valid_pass.append(password)

print(",".join(valid_pass))
