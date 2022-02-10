with open ("new_test.txt", mode = "w") as file:
    file.write("New Line\n")

with open ("new_test.txt", mode = "a") as file:
    file.write("Second Line\n")
    file.write("Third Line\n")
