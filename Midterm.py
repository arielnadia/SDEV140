# Magic 8 Ball Program

import random

MAGIC_BALL = [0] * 12

# Explain the program
def welcome():
    print("Ariel Merriman's Magic 8 Ball Program!")
    print('This program simulates a Magic 8 Ball, '\
          'where the user can ask a question and the '\
          'program will generate a random response.')
    print()

def main():
    # Call the functions
    welcome()
    MAGIC_BALL = magic_ball()
    # Declare the variables
    Index = 0
    Response = 'y'
    # Shake the magic 8 ball
    while Response == 'y' or Response == 'Y':
        Question = input('Ask the Magic 8 Ball a question: ')
        Number = ran_num()
        print(MAGIC_BALL[Number])
        Response = input('Play again? y/n ')    

# Save response to list
def magic_ball():
    Index = -1
    Responses = open('8_ball_responses.txt', 'r')
    for line in Responses:
        Index += 1
        MAGIC_BALL[Index] = line.rstrip('\n')
    Responses.close()
    return MAGIC_BALL

# Generate random number
def ran_num():
    Number = random.randint(1,12)
    return Number

# Run the program!
main()
