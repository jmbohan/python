# Does light edit mode effect git?
# I'm in git Bash
# This is a simple calculator app
# How do I get the access key to save?
# Testing git gui
# double test
def welcome():
    print('''
Welcome to Calculator
please enjoy...

    ''')
welcome()
# Define our function
def calculate():
    operation = input('''
    Please type in the math operation you think you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ^ for powers
    % for modulo
    ''')
    number_1 = int(input('enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    if operation == '+':
    # Addition
        print ('{} + {} = ' .format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
    # Subtraction
        print ('{} - {} = ' .format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
    # Multiplication
        print ('{} * {} = ' .format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
    # Division
        print ('{} / {} = ' .format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == '^':
    # Power
        print ('{} ^ {} = ' .format(number_1, number_2))
        print(number_1 ** number_2)

    elif operation == '%':
    # Division
        print ('{} % {} = ' .format(number_1, number_2))
        print(number_1 % number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

# Add again() function to calculate() function
    again()

# Define again() function to ask user if they want to use the calculator again
def again():

    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()

# Call calculate() outside of the function
calculate()
