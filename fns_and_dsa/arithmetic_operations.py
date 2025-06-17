def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations based on the given numbers and operation string.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or an error message if division by zero occurs
                      or an invalid operation is provided.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            # Handle division by zero
            return "Cannot divide by zero."
        else:
            return num1 / num2
    else:
        # Handle invalid operation input
        return "Invalid operation. Please choose from 'add', 'subtract', 'multiply', 'divide'."
