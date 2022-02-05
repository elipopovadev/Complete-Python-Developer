class User():
    def sign_in(self):
        print("logged in...")
        
    
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"{self.name} attacking with power of {self.power}.")
        

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f"{self.name} attacking with arrows: arrows left - {self.num_arrows}.")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
         Wizard.__init__(self, name, power)
         Archer.__init__(self, name, num_arrows)
         
    def attack(self):
        print(f"{self.name} attacking with power of {self.power}.")
        print(f"{self.name} attacking with arrows: arrows left - {self.num_arrows}.")

        

borg1 = HybridBorg("Borg_One", 500, 1000)
print(borg1.name)
print(borg1.power)
print(borg1.num_arrows)
print(borg1.attack())