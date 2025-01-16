# Prompt user for input
M = float(input('Enter the amount of water in kilograms: '))
initialTemperature = float(input('Enter the initial temperature in degrees Celsius: '))
finalTemperature = float(input('Enter the final temperature in degrees Celsius: '))

# Calculate energy
Q = M * (finalTemperature - initialTemperature) * 4184

# Display the result
print('The energy needed to heat the water is', Q,'joules.')
