minutes = eval(input("Enter the number of minutes: "))

days = minutes // (60 * 24)
years = days // 365
remaining_days = days % 365

print(f"{minutes} minutes is approximately {years} years and {remaining_days} days.")