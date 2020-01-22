# Pennies for Pay Program
print ("Ariel Merriman's Pennies for Pay Program!")
print ()

# Declare variables
PENNY = 0.01
Days = 1
Pennies = 1
DailyPay = 0
TotalPay = 0
Count = 1

# Receive input
Days = int(input('How many days have you worked? '))

# Validate input
while Days < 1:
    Days = int(input('ERROR: You cannot work less than 1 day. Please try again: '))

# Print table layout
print()
print('Days\tPay')
print('---------------')

# Run and display results
while Count <= Days:
    DailyPay = (float(Pennies * PENNY))
    print(Count, '\t $', format(DailyPay, ',.2f'), sep='')
    TotalPay += DailyPay
    Pennies *= 2
    Count += 1

print()
print('Total Pay for Days Worked: $', format(TotalPay, ',.2f'), sep='')
            
