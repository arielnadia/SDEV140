# Average of Numbers Program

# Explain program
def welcome():
    print("Ariel Merriman's Average of Numbers Program!")
    print('This program will read the numbers from the file '\
          "'numbers.txt' and calculate their average.")
    print()

def main():
    welcome()
    # Declare variables
    Total = 0
    Count = 0
    # Open file
    Numbers = open('numbers.txt', 'r')
    # Read file
    for line in Numbers:
        Num = int(line)
        Total += Num
        Count += 1
        print('Number', Count, 'is:', Num)
    # Close file
    Numbers.close()
    
    average(Total, Count)

# Calculate and display average
def average(Total, Count):
    Average = int(Total / Count)
    print('The average is:', Average)

# Run the program!
main()
