# Sales Tax Calculator

# Declare tax amounts
STATE_RATE = 0.05
COUNTY_RATE = 0.025

def main():
    print ('Ariel Merriman\'s Sales Tax Calculator!')
    print ()
    Subtotal = float(input('What is your total? ')) # Receive user input
    # Call the functions
    StateTax, CountyTax, TotalTax, TotalPurchase = Calculations(Subtotal)
    Results(Subtotal, StateTax, CountyTax ,TotalTax, TotalPurchase)

# Calculate tax amounts for subtotal and calculate grand total
def Calculations(Subtotal):
    StateTax = Subtotal * STATE_RATE
    CountyTax = Subtotal * COUNTY_RATE
    TotalTax = StateTax + CountyTax
    TotalPurchase = Subtotal + StateTax + CountyTax
    return StateTax, CountyTax, TotalTax, TotalPurchase

# Display results
def Results(Subtotal, StateTax, CountyTax, TotalTax, TotalPurchase):
    print ('Subtotal: $',format(Subtotal,'.2f'),sep='')
    print ('State Tax: $',format(StateTax,'.2f'),sep='')
    print ('County Tax: $',format(CountyTax,'.2f'),sep='')
    print ('Total Tax: $',format(TotalTax,'.2f'),sep='')
    print ('Total: $',format(TotalPurchase,'.2f'),sep='')

# Run the program!
main()

