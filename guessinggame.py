"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.



Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
"""

import random
#initialize variables

def start_game():
        
    # write your code inside this function.
    highscore = 1000 #initial high score
    playagain = input("Do you want to play a game?  ")
    
    while playagain.lower() != "n":
      numrange = 10 #the upper limit incase i want to change it later
      thenumber = random.randint(1,numrange)
      print("The number is: {}".format(thenumber)) #remove later
      print("The current High.. er low, score is {}.".format(highscore))
      thisguess = int(0)
      currenttries = int(0)
      
      print("Hello, I want to play a game\nYou are going to be punched in the throat\n*PUNCHEDINTHROAT*")
      print("How many more times you get punched in the throat depends on how many tries it takes you to guess a number between 1 and {}".format(numrange))
      
      while thisguess != thenumber:
          thisguess = int(input("What is your guess?  "))
          currenttries += 1
          if thisguess > thenumber:
            print("The number is lower")
          elif thisguess < thenumber:
            print("the number is higher")
            
      
      print("Well done, It only took you {} tries to guess my number!".format(currenttries))
      if currenttries < highscore:
        highscore = currenttries
      print("highscore is {}".format(highscore))
      playagain = input("Do you want to play again? ")
      
      


  # Kick off the program by calling the start_game function.
start_game()
  
