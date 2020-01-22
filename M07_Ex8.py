# Name Search Program

GIRLS = [0] * 200
BOYS = [0] * 200

def welcome():
    print("Ariel Merriman's Name Search Program!")
    print('This program allows the user to search for ' \
          'a name and returns whether the name is in ' \
          'the list of most popular baby names from 2000 ' \
          'through 2009.')
    print()

def main():
    # Call the functions
    welcome()
    GIRLS = girls()
    BOYS = boys()
    # Declare variables
    Index = 0
    Response = 'y'
    # Allow user to search names until they're done
    while Response == 'y' or Response == 'Y':
        Response = name_search()

# Save girl names to list
def girls():
    Index = -1
    Girl_Names = open('GirlNames.txt', 'r')
    for line in Girl_Names:
        Index += 1
        GIRLS[Index] = line.rstrip('\n')
    Girl_Names.close()
    return GIRLS

# Save boy names to list
def boys():
    Index = -1
    Boy_Names = open('BoyNames.txt', 'r')
    for line in Boy_Names:
        Index += 1
        BOYS[Index] = line.rstrip('\n')
    Boy_Names.close()
    return BOYS

# Receive user input and search for it in the lists
def name_search():
    Name = input('Enter a name: ')
    if Name in GIRLS:
        print(Name, 'was a popular girl name!')
    elif Name in BOYS:
        print(Name, 'was a popular boy name!')
    else:
        print(Name, 'was not found in either list.')
    Response = input('Try another? y/n ')
    return Response

# Run the program!
main()
    
