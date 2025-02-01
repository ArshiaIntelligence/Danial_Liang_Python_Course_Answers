amount = float(input('Enter the anual of investment: '))
interest_rate = float(input('Enter the interest rate:(in percent) ')) / 100
years = int(input('Enter the numbers of year: '))

future_value = amount * pow((1 + interest_rate), years)

print(future_value)