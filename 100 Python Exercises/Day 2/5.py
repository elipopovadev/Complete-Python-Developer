# 5. Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class MyClass():
    def __init__(self, input):
        self.input = input
    
    def getString(self):
        return str(self.input)
           
    def printString(self):
        result = self.getString()
        print(result.upper())
        

def test(input):
    my_class = MyClass(input)
    string = my_class.getString()
    print(string)
    my_class.printString()
    

test_input = input()
test(test_input)

