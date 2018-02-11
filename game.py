
# g = GuessingGame()

# g.rand_choice gives you the random number

# g.guess()  starts the game 


import random

class GuessingGame():
  
  def __init__(self):
    self.rand_choice = random.randint(0,10)
    
  def reset_random(self):
    print('Resetting random number')
    self.rand_choice = random.randint(0,10)
  
  def guess(self):
    user_guess = int(input("What is a random number between 0 and 10:"))
    
    if user_guess == self.rand_choice:
      print("that is the correnct number")
      
    else:
      if user_guess < self.rand_choice:
        print('wrong, guess agian.')
      else:
        print('guess lower')
    
