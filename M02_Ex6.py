# Sales Tax Calculator
print ('Ariel Merriman\'s Sales Tax Calculator')
# Declare tax amounts
STATE_RATE = 0.05
COUNTY_RATE = 0.025
Subtotal = 0
StateTax = 0
CountyTax = 0
TotalTax = 0
TotalPurchase = 0
# Receive user input
Subtotal = float(input('What is your total? '))
# Calculate tax amounts for subtotal
StateTax = Subtotal * STATE_RATE
CountyTax = Subtotal * COUNTY_RATE
TotalTax = StateTax + CountyTax
# Calculate grand total
TotalPurchase = Subtotal + StateTax + CountyTax
# Display results
print ('Subtotal: $',format(Subtotal,'.2f'),sep='')
print ('State Tax: $',format(StateTax,'.2f'),sep='')
print ('County Tax: $',format(CountyTax,'.2f'),sep='')
print ('Total Tax: $',format(TotalTax,'.2f'),sep='')
print ('Total: $',format(TotalPurchase,'.2f'),sep='')
