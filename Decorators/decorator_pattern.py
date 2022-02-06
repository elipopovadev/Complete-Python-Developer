def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("**********")
        func(*args, **kwargs)
        print("**********")
    return wrap_func

@my_decorator
def print_hello(greeting, emoji = ":)"):
    print(greeting, emoji)
    
print_hello("Hiiiiii")
