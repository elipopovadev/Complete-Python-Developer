def func (num1, num2): 
    try:
        return num1 / num2
    except(TypeError, ValueError) as error:
        raise error

print(func(1, "3"))
        