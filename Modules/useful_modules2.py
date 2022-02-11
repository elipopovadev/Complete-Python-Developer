import datetime
from time import time
from array import array

t1 = time()

print(datetime.datetime.now())
print(datetime.date.today())

t2 = time()
time_span = t2 - t1 # 0.0009882450103759766
print(time_span)

my_array = array('i', [1, 2, 3])
print(my_array) # array('i', [1, 2, 3])
