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
    play_again = "y" #initial play_again status
    num_range = int(10) #the upper limit incase i want to change it later
    best_score = num_range #initial best score set to the max range
    
    while play_again.lower() != "n":
      the_number = random.randint(1,num_range)
      
      #print("The number is: {}".format(the_number)) #put this here for debugging. commented out in final product
      
      print("The current best score is {}.".format(best_score))
      this_guess = int(0) #initialize the first guess
      current_tries = int(0) #initialize the number of tries
      
      print("Guess an integer between 1 and {}, I'll let you know for each guess if the number is higher or lower than your guess".format(num_range))
      
      while this_guess != the_number:
          #Check for valid integer input
          try:
            current_tries += 1  #invalid guesses still count as guesses!
            this_guess = int(input("What is guess number {}?  ".format(current_tries)))
          except ValueError:
            print("That isn't an integer, try again.")  
            continue  
          
          #check that the integer input is within proper range
          if (this_guess > num_range) or (this_guess < 1):
            print("That is outside the range, number must be between 1 and {}".format(num_range))
            continue
                   
          #Check if the guess is higher or lower than the number and let the user know
          if this_guess > the_number:
            print("The number is lower")
          elif this_guess < the_number:
            print("The number is higher")
            
      
      print("Well done, It only took you {} tries to guess my number!".format(current_tries))
      #Update and display the best score
      if current_tries < best_score:
        best_score = current_tries
      print("The best score is {}".format(best_score))
      
      #prompt for playing again, make sure they enter y or n
      play_again = input("Do you want to play again? (y/n)  ")
      while play_again.lower() not in ("n","y"):
        play_again = input("Please enter y or n:  ")
        

  # Kick off the program by calling the start_game function.
print("Welcome to the number guessing game!")  
start_game()
  
