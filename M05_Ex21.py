# Rock, Paper, Scissors Game

import random

#Explain program
def welcome():
    print("Ariel Merriman's Rock, Paper, Scissors Game!")
    print('This program simulates a game of rock, paper, scissors.')
    print()

def main():
    # Declare variables
    Player1 = ''
    Player2 = ''
    Result = 'y'
    # Call the functions
    welcome()
    while Result == 'tie' or Result == 'y':
        Player1 = pc_choice()
        Player2 = user_choice()
        Result = rules(Player1, Player2)
    print('Thanks for playing!')

# Generate PC choice
def pc_choice():
    Roll = random.randint(1, 3)
    if Roll == 1:
        Player1 = 'rock'
    elif Roll == 2:
        Player1 = 'paper'
    else:
        Player1 = 'scissors'
    return Player1

# Receive input for user choice
def user_choice():
    Player2 = input('Enter rock, paper, or scissors: ')
    return Player2

# Determine results
def rules(Player1, Player2):
    if Player1 == 'rock' and Player2 == 'scissors':
        print('Player 1 chose', Player1, 'and Player 2 chose', Player2,\
              'so Player 1 wins! Play again? (y/n) ')
        Result = input()
        return Result
    elif Player1 == 'paper' and Player2 == 'rock':
        print('Player 1 chose', Player1, 'and Player 2 chose', Player2,\
              'so Player 1 wins! Play again? (y/n) ')
        Result = input()
        return Result
    elif Player1 == 'scissors' and Player2 == 'paper':
        print('Player 1 chose', Player1, 'and Player 2 chose', Player2,\
              'so Player 1 wins! Play again? (y/n) ')
        Result = input()
        return Result
    elif Player1 == 'rock' and Player2 == 'paper':
        print('Player 1 chose', Player1, 'and Player 2 chose', Player2,\
              'so Player 2 wins! Play again? (y/n) ')
        Result = input()
        return Result
    elif Player1 == 'paper' and Player2 == 'scissors':
        print('Player 1 chose', Player1, 'and Player 2 chose', Player2,\
              'so Player 2 wins! Play again? (y/n) ')
        Result = input()
        return Result
    elif Player1 == 'scissors' and Player2 == 'rock':
        print('Player 1 chose', Player1, 'and Player 2 chose', Player2,\
              'so Player 2 wins! Play again? (y/n) ')
        Result = input()
        return Result
    else:
        print('Player 1 chose', Player1, 'and Player 2 chose', Player2,\
              'so it\'s a tie! Please try again.')
        Result = 'tie'
        return Result

# Run the program!    
main()
