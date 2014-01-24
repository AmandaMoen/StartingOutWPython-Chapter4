# May 26th, 2010
# CS110
# Amanda L. Moen
# 5. Software Sales
# A software company sells a package that retails for $99.
# Quantity discounts are given according to the following table:
#       Quantity        Discount
#       10-19           20%
#       20-49           30%
#       50-99           40%
#       100 or more     50%
# Write a program that asks the user to enter the number of packages
# purchased.  The program should then display the amount of the
# discount (if any) and the total amount of the purchase after the
# discount.

def main():
    # Ask the user to enter the number of packages purchased.
    quantity = input('Enter the number of packages purchased: ')

    # Determine the discount percentage.
    if quantity < 10:
        print 'No discount.'
        discount=1.0
    elif quantity < 20:
        print 'Your discount is 20%.'
        discount=0.8
    elif quantity < 50:
        print 'Your discount is 30%.'
        discount=0.7
    elif quantity < 100:
        print 'Your discount is 40%.'
        discount=0.6
    else:
        print 'Your discount is 50%.'
        discount=0.5

    # define 'total'
    total(quantity, discount)
    
    
def total(quantity, discount):
    # With no discount each package of software costs $99.00.
    # Calculate the total price with the discount
    total_amount = quantity * discount * 99.0
    # Calculate the total price before the discount
    full_price = quantity * 99.0
    print 'The amount of your discount is ', full_price - total_amount
    print 'Your total purchase price is ', total_amount

# Call the main function.
main()
