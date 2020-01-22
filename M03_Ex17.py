# Wi-Fi Diagnostic Tree
print ("Ariel Merriman's Wi-Fi Diagnostic Tree Program!")
print ()

# Run the program!
print ('Reboot the computer and try to connect.')
Response = input('Did that fix the problem? ')

if Response == 'no':
    print ('Reboot the router and try to connect.')
    Response = input('Did that fix the problem? ')
    if Response == 'no':
        print ('Make sure the cables between the router and modem are plugged in firmly.')
        Response = input('Did that fix the problem? ')
        if Response == 'no':
            print ('Move the router to a new location and try to connect.')
            Response = input('Did that fix the problem? ')
            if Response == 'no':
                print ('Get a new router.')
            else:
                print ('Yay!')
        else:
            print ('Yay!')
    else:
        print ('Yay!')
else:
    print ('Yay!')
