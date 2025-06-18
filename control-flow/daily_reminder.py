# daily_reminder.py

# Prompt for a single task description
task = input("Enter your task: ")

# Prompt for the task's priority (high, medium, low)
# Convert to lowercase to make the input case-insensitive for comparison
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound (yes or no)
# Convert to lowercase for case-insensitive comparison
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message part that depends on priority
priority_message = ""

# Process the task based on priority using a Match Case statement
match priority:
    case "high":
        priority_message = "high priority task"
    case "medium":
        priority_message = "medium priority task"
    case "low":
        priority_message = "low priority task"
    case _:
        # Handle unexpected priority input
        priority_message = "task of unspecified priority"

# Build the base reminder
reminder = f"Reminder: '{task}' is a {priority_message}"

# Use an if statement to modify the reminder if the task is time-bound
if time_bound == "yes":
    # Append the immediate attention message
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    # If not time-bound, just end the sentence normally.
    # We could also add specific non-time-bound phrasing here if desired.
    reminder += "."
else:
    reminder += " (Time-bound status unclear)."


# Provide a customized reminder
print(f"Reminder: '{task}' is a {priority_description}{time_sensitive_suffix}")
