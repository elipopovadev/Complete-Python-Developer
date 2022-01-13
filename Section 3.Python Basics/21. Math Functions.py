import operator

print(operator.abs(-10))  # print absolute value 10
print(round(10.4)) #print rounded value 10
print(round(10.5)) #print rounded value 10
print(round(10.51)) #print rounded value 11
print(round(10.6)) #print rounded value 11

print(operator.add(3, 4))  # a+b
print(operator.sub(10, 5))  # a-b
print(operator.mul(10, 2))  # a*b

print(operator.truediv(10, 4))  # 10/4
print(operator.floordiv(10, 4))  # 10//4
print(operator.mod(10, 3))  # 10%3
print(operator.pow(10, 2))  # 10**2

print(operator.lt(5, 10))  # check if a < b and returns bool
print(operator.le(5, 5))  # check if a <= b and returns bool
print(operator.eq(10, 10))  # check if a == b and returns bool

print(operator.gt(10, 5))  # check if a > b and returns bool
print(operator.ge(10, 10))  # check if a <= b and returns bool
print(operator.ne(10, 5))  # returns true if a is not equal to b
