# Ingredient Adjuster
print ('Ariel Merriman\'s Ingredient Adjuster')
# Declare variables
BASE_SUGAR = 1.5 / 48
BASE_BUTTER = 1 / 48
BASE_FLOUR = 2.75 / 48
Cookies = 0
Sugar = 0
Butter = 0
Flour = 0
# Receive user input
Cookies = int(input('How many cookies do you want to make? '))
# Calculate recipe
Sugar = BASE_SUGAR * Cookies
Butter = BASE_BUTTER * Cookies
Flour = BASE_FLOUR * Cookies
# Display results
print ('You will need:')
print (format(Sugar,'.2f'),'cups of sugar')
print (format(Butter,'.2f'),'cups of butter')
print (format(Flour,'.2f'),'cups of flour')
