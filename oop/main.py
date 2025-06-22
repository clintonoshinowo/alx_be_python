from polymorphism_demo import Shape, Rectangle, Circle
import math # Although math is imported in polymorphism_demo, it's good practice to keep it if needed here too, or if polymorphism_demo changes later.

def main():
    # Create instances of different shapes
    shapes = [
        Rectangle(10, 5), # A rectangle with length 10, width 5
        Circle(7)         # A circle with radius 7
    ]

    # Iterate through the list of shapes and print their areas.
    # This loop demonstrates polymorphism:
    # The 'area()' method is called on each 'shape' object,
    # but the specific implementation (Rectangle's area or Circle's area)
    # is executed based on the object's actual class.
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
