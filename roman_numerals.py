# May 16th, 2010
# CS110
# Amanda L. Moen
# 1. Roman Numerals
# Write a program that prompts the user to enter a number within
# the range of 1 through 10.  The program should display the Roman
# numeral version of that number.  If the number is outside the
# range of 1 through 10, the program should display an error
# message.  The following table shows the Roman numerals for the
# numbers 1 through 10:
#       Number      Roman Numeral
#       1           I
#       2           II
#       3           III
#       4           IV
#       5           V
#       6           VI
#       7           VII
#       8           VIII
#       9           IX
#       10          X

def main():
    # Ask the user to enter a number within the range of 1-10
    number = input('Enter a number within the range of 1 through 10: ')

    if number == 1:
        print 'The Roman Numeral is I.'
    elif number == 2:
        print 'The Roman Numeral is II.'
    elif number == 3:
        print 'The Roman Numeral is III.'
    elif number == 4:
        print 'The Roman Numeral is IV.'
    elif number == 5:
        print 'The Roman Numeral is V.'
    elif number == 6:
        print 'The Roman Numeral is VI.'
    elif number == 7:
        print 'The Roman Numeral is VII.'
    elif number == 8:
        print 'The Roman Numeral is VIII.'
    elif number == 9:
        print 'The Roman Numeral is IX.'
    elif number == 10:
        print 'The Roman Numeral is X.'
    else:
        print 'Error!'

# Call the main function.
main()
