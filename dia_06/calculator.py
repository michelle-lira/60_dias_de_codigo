"""
This program allows the user to choose to perform basic math operations 
as many times as they like. Are they:
    Addition
    Subtraction
    Multiplication
    Division
    Potentiation
    Module

Type the symbol corresponding to the operation you want to calculate 
on the screen. 
"""

def welcome():
    print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
-=-=-=-=-=  Welcome to Calculator!  =-=-=-=-=-
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
''')

def calculate():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ** for power
    % for modulo
    ''')

    if operation == '+':
        addition()

    elif operation == '-':
        subtraction()

    elif operation == '*':
        multiplication()

    elif operation == '/':
        division()

    elif operation == '**':
        power()

    elif operation == '%':
        modulo()
        
    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate function
    again()

def again():
    calc_again = input('''
    Do you want calculate again?
    Please type Y for YES or N for NO.
    ''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Ok, see you later :-)')
    else:
        again()

# Operations
def addition():
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    print(f'{number_1} + {number_2} = ')
    print(number_1 + number_2)

def subtraction():
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    print(f'{number_1} - {number_2} = ')
    print(number_1 - number_2)

def multiplication():
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    print(f'{number_1} * {number_2} = ')
    print(number_1 * number_2)

def division():
    try:
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
        result = number_1 / number_2

        if x / y:
            print(f'{number_1} / {number_2} = ')
            print(result)

    except ZeroDivisionError:
        print('''
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=
        Division by zero! Try again.
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-
        ''')
    else:
        print("Result is", result)
    finally:
        print("Executing finally clause")

def power():
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    print(f'{number_1} ** {number_2} = ')
    print(number_1 ** number_2)

def modulo():
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    print(f'{number_1} % {number_2} = ')
    print(number_1 % number_2)

welcome()
calculate()
