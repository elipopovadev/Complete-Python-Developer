import os

try:
    os.remove("my_new_file")
    print("Deleted!")
except FileNotFoundError:
    print("File already deleted!")
    