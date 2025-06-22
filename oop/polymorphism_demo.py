import math

class Shape:
    """
    Base class for different shapes.
    Defines a common interface for calculating area.
    """
    # Ensure this method is indented with exactly 4 spaces relative to 'class Shape:'
    def area(self):
        """
        Raises a NotImplementedError, indicating that derived classes
        must override this method to provide their specific area calculation.
        """
        # Ensure this statement is indented with exactly 8 spaces
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    """
    A derived class representing a rectangle.
    Inherits from Shape and overrides the area method.
    """
    # Ensure __init__ is indented with 4 spaces
    def __init__(self, length, width):
        # Ensure content is indented with 8 spaces
        self.length = length
        self.width = width

    # Ensure area is indented with 4 spaces
    def area(self):
        # Ensure content is indented with 8 spaces
        return self.length * self.width

class Circle(Shape):
    """
    A derived class representing a circle.
    Inherits from Shape and overrides the area method.
    """
    # Ensure __init__ is indented with 4 spaces
    def __init__(self, radius):
        # Ensure content is indented with 8 spaces
        self.radius = radius

    # Ensure area is indented with 4 spaces
    def area(self):
        # Ensure content is indented with 8 spaces
        return math.pi * (self.radius ** 2)
