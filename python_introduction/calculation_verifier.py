# calculation_verifier.py

# --- Example Input Values (matching the problem statement) ---
test_monthly_income = 5000.0
test_total_monthly_expenses = 4000.0
test_annual_interest_rate = 0.05 # 5% as a decimal

# --- Perform Calculations (same logic as finance_calculator.py) ---
calculated_monthly_savings = test_monthly_income - test_total_monthly_expenses
calculated_projected_annual_savings = (calculated_monthly_savings * 12) + \
                                      (calculated_monthly_savings * 12 * test_annual_interest_rate)

# --- Print Results for Verification ---
print(f"--- Verification Results ---")
print(f"Expected Monthly Savings: ${calculated_monthly_savings:.2f}")
print(f"Expected Projected Annual Savings: ${calculated_projected_annual_savings:.2f}")
print(f"--------------------------")

# You can now compare these outputs with the output of your finance_calculator.py
# when you provide it with 5000 and 4000 as input.

