def highes_even(li):
    li.sort(reverse=True)
    for num in li:
     if(num % 2 == 0):
      return num

print(highes_even([10, 2, 3, 4, 8, 11]))

#Another solution
def highes_function(li):
    evens = []
    for num in li:
        if(num % 2 == 0):
            evens.append((num))
    return max(evens)

print(highes_function([10, 2, 3, 4, 8, 11]))
