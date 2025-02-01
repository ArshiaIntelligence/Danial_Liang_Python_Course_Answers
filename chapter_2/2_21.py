monthly_saving = float(input('Enter the monthly saving amount: '))
annual_interest_rate = float(input('Enter the annual intrest rate: (in percent) '))
monthly_interest_rate = annual_interest_rate / 12
account_value = 0

for month in range(1, 7):
    account_value = (account_value + monthly_saving) * (1 + monthly_interest_rate)

print('Account value after 6 months:', '$',account_value)
