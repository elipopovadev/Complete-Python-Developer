i = 0
while i <= 50:
    print(i)
    i += 1
else:
 print('Everything is done!')

my_list = [1, 2, 3, 4]
j = -1
while j < len(my_list) - 1:
    j += 1
    if j == 1:
     continue
    print(my_list[j])

while True:
    response = input('Say something: ')
    if(response == 'bye'):
     break
