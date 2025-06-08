# finance_calculator.py

# --- User Input for Financial Details ---
# Prompt the user for their monthly income
# Convert the input to a float to handle decimal amounts
monthly_income = float(input("Enter your monthly income: "))

# Ask for their total monthly expenses
# Convert the input to a float
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# --- Calculate Monthly Savings ---
monthly_savings = monthly_income - total_monthly_expenses

# --- Project Annual Savings ---
# Assume a simple annual interest rate of 5% (0.05)
annual_interest_rate = 0.05

# Calculate the projected savings after one year, incorporating the interest.
# Formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# --- Output Results ---
# Display the user's monthly savings
print(f"Your monthly savings are ${monthly_savings:.2f}.") # .2f for 2 decimal places

# Display the projected annual savings after including interest
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.") # .2f for 2 decimal places
