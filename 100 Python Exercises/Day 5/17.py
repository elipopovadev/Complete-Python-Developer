''' Question 17:
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100

Then, the output should be:
500 '''

balance = 0
while True:
    input_ = input()
    if input_ == "Done":
        print(balance)
        break
    list_operation = input_.split(" ")
    operation = list_operation[0]
    amount = int(list_operation[1])
    if operation == "D":
        balance += amount
    elif operation == "W":
        balance -= amount
