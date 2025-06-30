# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division, handling potential ZeroDivisionError and ValueError.

    Args:
        numerator: The top number in the division.
        denominator: The bottom number in the division.

    Returns:
        A string indicating the result of the division or an error message.
    """
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
