# pattern_drawing.py

# Prompt the user for the pattern size
# Convert the input to an integer
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop (to iterate through rows)
row = 0

# Use a while loop to iterate through each row of the pattern
# The loop continues as long as 'row' is less than 'size'
while row < size:
    # Use a for loop to print asterisks (*) side by side for the current row
    # The range(size) iterates 'size' times, representing the columns
    for col in range(size):
        # Print an asterisk without adding a new line at the end
        print("*", end="")
    
    # After completing all columns for the current row, print a newline character
    # This moves the cursor to the next line for the next row of asterisks
    print()
    
    # Increment the row counter to move to the next row
    row += 1
