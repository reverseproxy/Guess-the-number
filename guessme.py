# This section imports all the necessary tools and functions for this to work, "from" specifies a function in a specific toolkit, and "import" just imports the entire toolkit
from prompt_toolkit import prompt
from datetime import date
import random
import math

# Asks the user the year they were born, the ** int ** notion before it turns it into an integer for formula
value = int(input ('What month were you born in? - '))

# Produces a random number, the current year, and tells the computer to add together a random number and the year, and minus the user entry
random_number = random.randint(1,100)
current_year = date.today().year
computer_guess = current_year - value + random_number

# This is the prompt for the game input to enter their
game_guess = int(input('What is the number I am thinking of ? : '))

# This displays the number required to win - used simply for verification for script (or cheaters)
print('This is the winning number if youre a cheater, otherwise keep guessing')
print(computer_guess)

while True:
    if game_guess != computer_guess:
        game_guess = int(input('Try again : '))
        if game_guess == computer_guess:
            break
print("Yey, you win!")


# NOTES
# Mathematical formulas weren't working properly because they need to be marked as Integers, otherwise it juse sees the input as a string and not as a number, so keeps repeating the question even if correct
