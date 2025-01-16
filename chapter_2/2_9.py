temperature = float(input('Enter the temperature in Fahrenheit (-58 to 41): '))
wind_speed = float(input('Enter the wind speed in miles per hour (>= 2): '))

if -58 <= temperature <= 41 and wind_speed >= 2:

    twc = 35.74 + (0.6215 * temperature) - (35.75 * (pow(wind_speed, 0.16))) + ((0.4275 * temperature) * (pow(wind_speed, 0.16)))
    print('The wind-chill temperature is:', twc,'°F')

else:
    print('Invalid input. Please ensure the temperature is between -58°F and 41°F and wind speed is at least 2 mph.')
