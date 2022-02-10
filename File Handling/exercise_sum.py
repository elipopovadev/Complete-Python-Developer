with open("test.txt", mode = "r") as my_file:
    int_list = list(map(int, ([element for element in my_file.readlines()])))
    print(sum(int_list))
    