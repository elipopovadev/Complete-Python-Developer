class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name, age):
      if PlayerCharacter.membership == True:
        self.name = name # attributes
        self.age = age
        
    def shout(self):
        print(f"my name is {self.name}")
    
    def run(self):
        print(f"my name is {self.name}")
    
    
player1 = PlayerCharacter("Tom", 30)
player2 = PlayerCharacter("Anabel", 20)
player1.run()
player2.shout()
