books = ['Peter Pan', 'The H. P. Lovecraft collection', 'Oliver Twist']
print(books[0])  # Peter Pan
print(books[2])  # Oliver Twist

print(books[0:1])  # ['Peter Pan']
print(books[0:2])  # ['Peter Pan', 'The H. P. Lovecraft collection']
print(books[::-1])  # Reverse order
print(books[::-2])  # ['Oliver Twist', 'Peter Pan']
print(books[-1])  # Oliver Twist
print(books[-2])  # The H. P. Lovecraft collection

print(books)  # ['Peter Pan', 'The H. P. Lovecraft collection', 'Oliver Twist']
books[0] = 'Hard Times'
# ['Hard Times', 'The H. P. Lovecraft collection', 'Oliver Twist']
print(books)

collection = books
collection[0] = 'David Copperfield'
# ['David Copperfield', 'The H. P. Lovecraft collection', 'Oliver Twist'], because list is a ref type
print(books)
# ['David Copperfield', 'The H. P. Lovecraft collection', 'Oliver Twist'], because list is a ref type
print(collection)

new_collection = collection[:]  # we create a new list
new_collection[0] = 'Bleak house'
# ['Bleak house', 'The H. P. Lovecraft collection', 'Oliver Twist']
print(new_collection)
# is not changed ['David Copperfield', 'The H. P. Lovecraft collection', 'Oliver Twist']
print(collection)
