# May 26th, 2010
# CS110
# Amanda L. Moen
# 3. Mass and Weight
# Scientists measure an object's mass in kilograms and its weight in newtons.
# If you know the amount of mass of an object in kilograms, you can calculate
# its weight in newtons with the following formula:
#       weight = mass X 9.8
# Write a program that asks the user to enter an object's mass, and then
# calculates its weight.  If the object weighs more than 1000 newtons,
# display a message indicating that it is too heavy.  If the object weighs
# less than 10 newtons, display a message indicating that it is too light.

def main():
    # Ask the user to enter an object's mass.
    mass = input("Enter an object's mass in kilograms: ")
    function(mass)

def function(mass):
    

    # Calculate the weight in newtons (weight=mass*9.8)
    weight = mass * 9.8

    if weight >= 1000:
        print 'The object is too heavy.'
    elif weight <= 10:
        print 'The object is too light.'
    else:
        print 'The corresponding weight in newtons is ', weight, 'newtons.'

    

# Call the main function.
main()
