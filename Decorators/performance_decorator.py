import time

def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f"took {t2-t1}s")
        return result
    return wrap_func

@performance   
def long_time():
    for i in range(100000000):
        i * 5
 
long_time()