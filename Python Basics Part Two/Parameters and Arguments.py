#Parameters
def say_hello(name, age):
    print(f'Hello, I am {name} and I am {age} years old.')

#Default Parameters
def say_something(name='Andrei', age=20):
    print(f'Hello, I am {name} and I am not {age} years old.')

say_something()

#Positional Arguments
say_hello('Elena', 14)
say_hello('John', 10)

#Keyword Arguments
say_hello(name='Peter', age=20)
say_hello(age=10, name='Ana')
