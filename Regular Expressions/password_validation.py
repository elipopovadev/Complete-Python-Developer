import re
# At least 8 char long 
# Contain any sort letters, numbers and $%#@
# Has to end with number

pattern = re.compile(r"(^[\w$%#@]{7,}[\d]+$)")
passwords = ["edgde4gtg%@3", "ffefefe%%%4", "$5swdwd#fe63", "---fefe---", "12er5"]

print("Valid passwords are:")
for password in passwords:
    if pattern.match(password):
        print(password) # edgde4gtg%@3, ffefefe%%%4, $5swdwd#fe63
        