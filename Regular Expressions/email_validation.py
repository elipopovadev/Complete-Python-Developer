import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
emails = ["emiliq_g@gmail.com", "ivanP@gmail.com", "124@"]
for email in emails:
    if pattern.match(email):
        print(email)
        