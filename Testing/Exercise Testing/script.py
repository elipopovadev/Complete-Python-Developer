import random 

def check_input(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("you are a genius!")
            return True
    else:
        print("hey, I said 1~10")
        return False
        
if __name__ == "__main__":       
    answer = random.randint(1, 10)
    while True:
       try:    
          guess = int(input("guess a number 1~10:  "))     
          check_input(guess, answer)
          if guess == answer:
              break
        
       except ValueError:
          print("Please, enter a number")
          continue
        