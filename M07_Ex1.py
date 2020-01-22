# Total Sales Program

WEEK = 7

# Explain program
def welcome():
    print("Ariel Merriman's Total Sales Program!")
    print('This program allows the user to input the ' \
          'amount of sales at one store for each day ' \
          'of the week, and then calculates the total ' \
          'sales for the week.')
    print()

def main():
    welcome()
    # Declare variables
    Sales = [0] * WEEK
    Index = 0
    Total= 0
    # Receive user input
    print('Enter the sales for each day:')
    while Index < WEEK:
        print('Day #', Index + 1, ': ', sep ='', end='')
        Sales[Index] = float(input())
        Index +=1
    Index = WEEK - 1
    # Calculate and display total
    while Index >= 0:
        Total += Sales[Index]
        Index -= 1
    print('Total sales for the week: $', format(Total, ',.2f'), sep='')
    

# Run the program!
main()
