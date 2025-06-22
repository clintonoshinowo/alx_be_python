from class_static_methods_demo import Calculator

def main():
    # Using the static method
    # Static methods can be called directly on the class without an instance.
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    # Class methods can also be called directly on the class.
    # The 'cls' parameter will automatically receive the Calculator class.
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
