import re

pattern = re.compile(r"([A-Za-z]).([a])")
text = 'Search this inside ot this text please!'

a = pattern.search(text)
print(a.group()) # Sea
b = pattern.findall(text) 
print(b) # [('S', 'a'), ('l', 'a')]
c = pattern.fullmatch(text)
print(c) # None
d = pattern.match(text)
print(d) # None
