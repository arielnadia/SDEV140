# Maximum of Two Values Program

# Explain program
def welcome():
    print("Ariel Merriman's Maximum of Two Values Program!")
    print('This program will display the greater of two numbers',\
          'entered by the user.')
    print()

# Receive input
def main():
    welcome()
    num1 = int(input('Enter a number. '))
    num2 = int(input('Enter another number. '))
    max(num1, num2)

# Determine larger number and display results
def max(num1, num2):
    if num1 > num2:
        print('The greater number is', num1)
    else:
        print('The greater number is', num2)

# Run the program!
main()
