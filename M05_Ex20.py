# Random Number Guessing Game

import random

# Explain program
def welcome():
    print("Ariel Merriman's Random Number Guessing Game!")
    print('This program generates a random number and prompts the user',\
          'to guess the number.')
    print()

def main():
    # Declare variables
    Number = 0
    Response = ''
    # Call the functions
    welcome()
    Number = ran_num()
    Response = how_close(Number)
    while Response == 'y':
        Number = ran_num()
        Response = how_close(Number)
    print('Thanks for playing!')

# Generate random number
def ran_num():
    Number = random.randint(1, 10)
    return Number

def how_close(Number):
    # Declare variables
    Guess = 99
    Count = 0
    # Receive and check input
    while Guess != Number and Guess != 0:
        Guess = int(input('Enter a number from 1 - 10, or enter 0 to quit: '))
        if Guess > Number:
            Count += 1
            print('Too high, try again.')
        elif Guess < Number and Guess != 0:
            Count +=1
            print('Too low, try again.')
        elif Guess == Number:
            Count += 1
            print('Congratulations, you guessed it after', Count,\
                  'tries! Play again? y/n ')
            Response = input()
            return Response
        else:
            return ''

# Run the program!
main()
    
