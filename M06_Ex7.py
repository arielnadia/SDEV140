# Random Number File Writer Program

import random

# Explain program
def welcome():
    print("Ariel Merriman's Random Number File Writer Program!")
    print('This program will create a user-specified number of '\
          'random numbers between 1 and 500 and save them to '\
          "a file named 'randoms.txt'.")
    print()

def main():
    welcome()
    # Initialize the counter
    Count = 1
    # Receive user input
    Amount = int(input('How many random numbers would you like? '))
    # Open file
    Random_File = open('randoms.txt', 'w')
    while Count <= Amount:
        Number, Count = generator(Count)
        Random_File.write(str(Number) + '\n')
    # Close file
    Random_File.close()
    print("The numbers have been saved to the file 'randoms.txt'.")

# Generate the random numbers
def generator(Count):
    Number = random.randint(1, 500)
    Count += 1
    return Number, Count

# Run the program!
main()
