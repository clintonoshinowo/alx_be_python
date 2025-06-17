from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and displays the current date and time in a specific format.
    """
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    # %Y for year with century, %m for month as zero-padded decimal, %d for day of month,
    # %H for hour (24-hour clock), %M for minute, %S for second.
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted current date and time
    print(f"Current date and time: {formatted_current_date}")
    
    # Return the datetime object for potential use in other functions
    return current_date

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date,
    and prints it in a specific format.
    """
    # Get the current date (we'll assume today's date for calculation base)
    # This also uses datetime.now() to ensure it's truly current
    current_date_for_future_calc = datetime.now()

    # Prompt the user to enter a number of days
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")
        return # Exit the function if input is not a valid integer

    # Calculate the future date by adding the specified number of days
    # timedelta is used to represent a duration
    future_date = current_date_for_future_calc + timedelta(days=days_to_add)
    
    # Format the future date as "YYYY-MM-DD"
    # %Y for year, %m for month, %d for day
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the formatted future date
    print(f"Future date: {formatted_future_date}")

# Main execution block
if __name__ == "__main__":
    # Call the function to display current date and time
    display_current_datetime()
    
    # Call the function to calculate and display a future date
    calculate_future_date()
