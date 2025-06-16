# multiplication_table.py

# Prompt the user to input a number
# Convert the input to an integer, as multiplication tables usually involve whole numbers.
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using a for loop
# The range(1, 11) generates numbers from 1 up to (but not including) 11, i.e., 1 to 10.
for i in range(1, 11):
    # Calculate the product of the user's number and the current loop iterator
    product = number * i
    # Print each line of the multiplication table in the format "X * Y = Z"
    print(f"{number} * {i} = {product}")
