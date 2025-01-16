# Financial Application: Investment Amount

final_account_value = float(input("Enter the final account value: "))
annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
number_of_years = float(input("Enter the number of years: "))

monthly_interest_rate = (annual_interest_rate / 100) / 12
number_of_months = number_of_years * 12

initial_deposit_amount = final_account_value / ((1 + monthly_interest_rate) ** number_of_months)

print('The initial deposit amount needed is:', '$', initial_deposit_amount)