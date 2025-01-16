v0 = float(input('Enter the starting velocity (v0) in meters/second: '))
v1 = float(input('Enter the ending velocity (v1) in meters/second: '))
t = float(input('Enter the time span (t) in seconds: '))

# Calculate average acceleration
a = (v1 - v0) / t

# Display the result
print('The average acceleration is', a, 'meters/second²')