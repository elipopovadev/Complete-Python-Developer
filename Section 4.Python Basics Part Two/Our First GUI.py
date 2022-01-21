picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for row in range(len(picture)):
    for col in range(len(picture[row])):
        if picture[row][col] == 1:
         print('*', end = '')
        else:
         print(' ', end = '')
    print()
    
# Another way
print()

for line in picture:
    for pixel in line:
        if pixel == 1:
         print('*', end = '')
        else:
         print(' ', end = '')
    print()
