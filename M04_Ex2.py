# Calories Burned Program
print ("Ariel Merriman's Calories Burned Program!")
print ()

# Declare variables
CAL_PER_MIN = 4.2
Calories = 0
Minutes = 10

# Exercise
while Minutes <= 30:
    Calories = int(CAL_PER_MIN * Minutes)
    print('It has been', Minutes, 'minutes and you have burned', \
          Calories, 'calories. Keep at it!')
    Minutes = Minutes + 5
