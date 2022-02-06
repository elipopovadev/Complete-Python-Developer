# Decorator 
def my_decorator(func):
    def wrap_func():
        print("**********")
        func()
        print("**********")
    return wrap_func

@my_decorator
def print_hello():
    print("Heloooooo")
    
@my_decorator
def print_bye():
    print("See ya later")
    
print_hello()
print_bye()