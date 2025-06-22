class Calculator:
    """
    A class demonstrating the use of static methods and class methods.
    """
    # Class Attribute: Shared by all instances and the class itself.
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: add(a, b)
        This method performs a simple addition of two numbers.
        It does NOT take 'self' or 'cls' as its first argument,
        as it does not need access to instance-specific data or class-specific data/methods.
        It's essentially a regular function logically grouped within the class.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: multiply(cls, a, b)
        This method performs multiplication of two numbers.
        It takes 'cls' (conventionally 'cls') as its first argument,
        which refers to the class itself (e.g., Calculator).
        This allows it to access class attributes (like calculation_type)
        or call other class methods.
        """
        # Accessing the class attribute using 'cls'
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
