def fib(number):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(number - 1):
        c = a + b
        a = b
        b = c
        yield c
        
for element in fib(10):
    print(element)


# with List
def fib2(number):
    result = []
    a = 0
    b = 1
    result.append(a)
    result.append(b)
    for i in range(number - 1):
        c = a + b
        a = b
        b = c
        result.append(c)
    return result

print(fib2(10))