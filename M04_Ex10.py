# Tuition Increase Program
print ("Ariel Merriman's Tuition Increase Program!")
print ()

# Declare variables
INCREASE = 0.03
Tuition = 8000.00
Count = 1

# Run and display results
while Count <= 5:
    Tuition = (Tuition * INCREASE) + Tuition
    print('Tuition in ', Count, ' year(s): $', format(Tuition, ',.2f'), sep='')
    Count += 1
