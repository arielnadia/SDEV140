# Exception Handling Program

# Explain program
def welcome():
    print("Ariel Merriman's Exception Handling Program!")
    print('This program will read the numbers from the file '\
          "'numbers.txt' and calculate their average.")
    print()

def main():
    welcome()
    # Declare variables
    Total = 0
    Count = 0
    try:
        # Open file
        Numbers = open('numbers.txt', 'r')
        # Read file
        try:
            for line in Numbers:
                Num = int(line)
                Total += Num
                Count += 1
                print('Number', Count, 'is:', Num)
            average(Total, Count)
        except ValueError:
            print('!!ValueError detected!!')
        # Close file
        Numbers.close()
    except IOError:
        print('!!IOError detected!!')

# Calculate and display average
def average(Total, Count):
    Average = int(Total / Count)
    print('The average is:', Average)

# Run the program!
main()
