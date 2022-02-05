class PlayerCharacter:
    def __init__(self, name, age):
       self.name = name
       self.age = age
       
    def run(self):
        print(f"{self.name} is running...")
    
    def speak(self):
        print(f"I am {self.name} and I am {self.age} years old.")
        

player1 = PlayerCharacter("Andrei", 100)
player2 = PlayerCharacter("Elena", 20)
player1.speak()
player2.speak()
player1.run()
player2.run()