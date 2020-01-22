# Car Class Program

import car

# Explain the program
def welcome():
    print("Ariel Merriman's Car Class Program!")
    print("This program creates a car object and reports the car's "\
          'speed after accelerating five times and braking five times.')
    print()

def main():
    welcome()
    # Create the car object
    Vehicle = car.Car(2007, 'Prius')
    print('The car is a: ', Vehicle.get_year_model(), Vehicle.get_make())
    print()
    Speed = Vehicle.get_speed()

    # Accelerate the car five times
    for count in range(5):
        print('Accelerating ...')
        Vehicle.accelerate(Speed)
        print(Vehicle.get_speed(), 'MPH')

    # This is just for the sake of appearance
    print()
    print('Resting ...')
    print()

    # Brake the car five times
    for count in range(5):
        print('Braking ...')
        Vehicle.brake(Speed)
        print(Vehicle.get_speed(), 'MPH')
    
# Run the program!
main()
