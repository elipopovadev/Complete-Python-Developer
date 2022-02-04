def super_func(*args):
    total = sum(args)
    print(total)
    
super_func(1, 2, 3, 4)

def super_func2(**kwargs):
    total = 0
    for value in kwargs.values():
        total += value
    print(total)
    
super_func2(num1 = 1, num2 = 2, num3 = 3, num4 = 4)