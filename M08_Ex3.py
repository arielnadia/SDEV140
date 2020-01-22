# Date Printer Program

# Explain the program
def welcome():
    print("Ariel Merriman's Date Printer Program!")
    print('This program will allow the user to input a date '\
          'in numerical format and then output that same date '\
          'with words.')
    print()

def main():
    # Receive input and convert to list
    Date = input("Enter today's date in the format mm/dd/yyyy: ")
    Date_List = Date.split('/')
    # Convert month to text format
    if Date_List[0] == '01':
        Date_List[0] = 'January'
    elif Date_List[0] == '02':
        Date_List[0] = 'February'
    elif Date_List[0] == '03':
        Date_List[0] = 'March'
    elif Date_List[0] == '04':
        Date_List[0] = 'April'
    elif Date_List[0] == '05':
        Date_List[0] = 'May'
    elif Date_List[0] == '06':
        Date_List[0] = 'June'
    elif Date_List[0] == '07':
        Date_List[0] = 'July'
    elif Date_List[0] == '08':
        Date_List[0] = 'August'
    elif Date_List[0] == '09':
        Date_List[0] = 'September'
    elif Date_List[0] == '10':
        Date_List[0] = 'October'
    elif Date_List[0] == '11':
        Date_List[0] = 'November'
    else:
        Date_List[0] = 'December'
    # Display results
    print("Today's Date is: " + str(Date_List[0]) + ' ' + str(Date_List[1]) + ', ' + str(Date_List[2])\
          + '.')

# Run the program!
main()
