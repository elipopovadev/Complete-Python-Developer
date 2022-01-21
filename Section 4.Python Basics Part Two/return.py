def sum(number1, number2):
    def another_funcion(num1, num2):
        return num1 + num2
    return another_funcion(number1, number2)

def multiplication(number1, number2):
    return number1 * number2

total = sum(10,30)
print(total)
result = multiplication(20, 3)
print(result)