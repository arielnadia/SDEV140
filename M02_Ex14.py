# Compound Interest Calculator
print ('Ariel Merriman\'s Compound Interest Calculator')
# Declare variables
Deposit = 0
APY = 0
Compound = 0
Years = 0
FinalTotal = 0
# Receive input
Deposit = float(input('What is your initial deposit amount? '))
APY = float(input('What is the annual interest rate? '))
Compound = int(input('How many times is interest compounded per year? '))
Years = int(input('How many years will you let it sit? '))
# Calculations
APY = APY/100 #converts interest rate to decimal
P = Deposit
r = APY
n = Compound
t = Years
A = P*(1 + r/n)**(n*t)
FinalTotal = A
# Display results
print ('If you deposit $',format(Deposit,'.2f'),sep='')
print ('At an APY of ' + str(format((APY*100),'.2f')) + '%',sep='')
print ('Which is compounded',Compound,'times per year')
print ('And you let it sit for',Years,'years')
print ('It will be worth $',format(FinalTotal,'.2f'),sep='')
