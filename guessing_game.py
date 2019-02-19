"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after youfork the snapshot of this workspace.

"""

import random
n = random.randint(1,9)

# 1. Display an intro/welcome message to the player.

print("Well, Hello There! Welcome to Guessing Number Quiz!" + "\n")

#2. Store a random number as the answer/solution.
answer= int(input("Guess the number! Oh and please only type numeric value from 1-9!>>   "))

attempt_count = 1

def start_game():
    try:
        answer= int(input("Guess the number! Oh and please only type numeric value from 1-9!>>   "))
    except ValueError:
        print("it's not a valid number, please try again.")
        
    """Psuedo-code Hints
    
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
    # write your code inside this function.

while n != answer:
    if answer > n:
        print("It's lower")
        attempt_count += 1
        answer= int(input("Guess the number! Oh and please only type numeric value!>>   "))
    elif answer < n:
        print("It's higher")
        attempt_count += 1
        answer= int(input("Guess the number! Oh and please only type numeric value!>>   "))
    else:
        print("Got it!")
        break
        attempt_count += 1
    
    
print("You have guessed the number with {} attempts! Well done you! \n -------END GAME-------".format(attempt_count))

# Kick off the program by calling the start_game function.

start_game()
