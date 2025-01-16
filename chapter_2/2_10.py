v = float(input('Enter the take-off speed (v) in meters/second (m/s): '))
a = float(input('Enter the acceleration (a) in meters/second squared (m/s²): '))

length = (pow(v, 2)) / (2 * a)

print('The minimum runway length needed for take-off is:', length, 'meters')