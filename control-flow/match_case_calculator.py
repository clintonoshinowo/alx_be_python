# match_case_calculator.py

# Prompt the user to input two numbers
# Use float() to allow for decimal numbers in calculations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the type of operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using a match case statement
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        # Handle division by zero
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        # Handle invalid operation input
        print("Invalid operation. Please choose from +, -, *, /.")
