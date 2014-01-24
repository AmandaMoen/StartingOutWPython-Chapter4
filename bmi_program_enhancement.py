# May 26th, 2010
# CS110
# Amanda L. Moen
# 7. Body Mass Index Program Enhancement
# In programming Exercise #6 in Chapter 3 you were asked to write
# a program that calculates a person's body mass index (BMI).
# Recall from that exercise that the BMI is often used to
# determine whether a person with a sedentary lifestyle is
# overweight or underweight for their height.  A person's BMI
# is calculated with the formula
#       BMI = weight X 703/height^2
# where weight is measured in pounds and height is measured in
# inches.  Enhance the program so it displays a message indicating
# whether the person has optimal weight, is underweight, or is
# overweight.  A sedentary person's weight is considered to be
# optimal if his or her BMI is between 18.5 and 25.  If the BMI
# is less than 18.5, the person is considered to be underweight.
# If the BMI value is greater than 25, the person is considered
# to be overweight.

def main():
    # Ask for the user's weight in pounds.
    weight = input('Please enter your weight in pounds: ')

    # Ask for the user's height in inches.
    height = input('Please enter your height in inches: ')

    # Calculate the BMI (BMI = weight*703/height^2)
    BMI = (weight * 703.0) / (height*height)
    print 'Your BMI is %.1f' % BMI

    # Determine whether the user is underweight, overweight, or optimal
    if BMI < 18.5:
        print 'You are underweight.'
    elif BMI > 25:
        print 'It would appear that you are overweight.'
    else:
        print 'You are at an optimal weight.'

# Call the main function.
main()
