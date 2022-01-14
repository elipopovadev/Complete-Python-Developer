username = input('Enter your name: ')
password = input('Enter your password: ')

password_len = len(password)
password_secret = '*' * password_len

print(f'Your name is: {username} and your {password_secret} is {password_len} letters long.')


