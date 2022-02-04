def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:', x)

    inner()
    print('outer', x)


outer()

# Another example for Closure
def getFibonator():
    prevNum = 0
    currentNum = 1

    def inner():
        nonlocal prevNum, currentNum
        nextNum = prevNum + currentNum
        prevNum = currentNum
        currentNum = nextNum
        return (prevNum)

    return inner


counter = getFibonator()
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())


# Another example for Closure
def sum():
    number = 0

    def inner():
        nonlocal number
        number += 1
        return (number)

    return inner


new_counter = sum()
print(new_counter())
print(new_counter())
print(new_counter())
