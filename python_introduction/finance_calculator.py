# finance_calculator.py

# Step 1: Get user input
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Step 2: Calculate monthly savings
monthly_savings = income - expenses

# Step 3: Project annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Step 4: Print results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
