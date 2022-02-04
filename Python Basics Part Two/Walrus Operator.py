a = 'heloooooooooo'


def check_length(a):
 if((n := len(a)) > 10):
    print(f'Too long {n} elements')


def remove_function(a):
    while((n := len(a)) >= 1):
        print(n)
        a = a[:-1]


check_length(a)
print(remove_function(a))
