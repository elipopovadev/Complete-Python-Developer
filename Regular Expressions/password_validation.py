import re
# At least 8 char long 
# Contain any sort letters, numbers and $%#@

pattern = re.compile(r"(^[\w$%#@]{7}[\w$%#@]+$)")
passwords = ["edgde4gtg%@", "ffefefe%%%", "$5swdwd#fe", "---fefe---", "12er"]

print("Valid passwords are:")
for password in passwords:
    if pattern.match(password):
        print(password) # edgde4gtg%@, ffefefe%%%, $5swdwd#fe
        