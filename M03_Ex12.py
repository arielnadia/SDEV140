# Software Sales Program
print ("Ariel Merriman's Software Sales Program!")
print ()

# Declare variables
RATE_1 = 0.10
RATE_2 = 0.20
RATE_3 = 0.30
RATE_4 = 0.40

Quantity = 0
Discount = 0
Rate = 0.0
Subtotal = 0.0
Total = 0.0

# Receive input
Quantity = int(input('How many packages would you like to buy? '))
Subtotal = Quantity * 99

# Calculate and display results
if Quantity >= 10 and Quantity <= 19:
    Rate = RATE_1
    Discount = Subtotal * Rate
    Total = Subtotal - Discount
    print ('Your ' + str(format((Rate * 100), '.0f')), '% discount is: $', format(Discount, ',.2f'), sep='')
    print ('Your total after discount is: $', format(Total, ',.2f'), sep='')
elif Quantity >= 20 and Quantity <= 49:
    Rate = RATE_2
    Discount = Subtotal * Rate
    Total = Subtotal - Discount
    print ('Your ' + str(format((Rate * 100), '.0f')), '% discount is: $', format(Discount, ',.2f'), sep='')
    print ('Your total after discount is: $', format(Total, ',.2f'), sep='')
elif Quantity >= 50 and Quantity <= 99:
    Rate = RATE_3
    Discount = Subtotal * Rate
    Total = Subtotal - Discount
    print ('Your ' + str(format((Rate * 100), '.0f')), '% discount is: $', format(Discount, ',.2f'), sep='')
    print ('Your total after discount is: $', format(Total, ',.2f'), sep='')
elif Quantity > 100:
    Rate = RATE_4
    Discount = Subtotal * Rate
    Total = Subtotal - Discount
    print ('Your ' + str(format((Rate * 100), '.0f')), '% discount is: $', format(Discount, ',.2f'), sep='')
    print ('Your total after discount is: $', format(Total, ',.2f'), sep='')
else:
    print ('Your total is: $', format(Subtotal, ',.2f'), sep='')
    
