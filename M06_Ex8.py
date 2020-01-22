# Random Number File Reader Program

# Explain program
def welcome():
    print("Ariel Merriman's Random Number File Reader Program!")
    print('This program will read and display the random numbers '\
          "from the 'randoms.txt' file along with their sum.")
    print()

def main():
    welcome()
    # Declare variables
    Total = 0
    Count = 0
    # Open file
    Random_File = open('randoms.txt', 'r')
    # Read file and process data
    for line in Random_File:
        Count += 1
        Num = int(line)
        print('#' + str(Count) + ': ' + str(Num))
        Total += Num
    print('The sum of the', Count, 'random numbers is:', Total)
    # Close file
    Random_File.close()

# Run the program!
main()
