text = '01234567'
print(text[0])  # print 0
print(text[7])  # print 7

#print(text[8]) IndexError: string index out of range

print(text[-1])  # print 7
print(text[-2])  # print 6

# text[start:stop:stepover]
print(text[0:2])  # print 01
print(text[2:])  # starts from index 2; print 234567
print(text[:8])  # 01234567
print(text[0:8:2])  # 0246
print(text[0:8:3])  # 036

# Reverse string
print(text[::-1])  # 76543210
