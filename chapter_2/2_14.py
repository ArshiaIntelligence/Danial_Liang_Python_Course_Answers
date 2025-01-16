# Prompt user for input
x1, y1 = map(float, input('Enter the coordinates of point 1 (x1, y1): ').split())
x2, y2 = map(float, input('Enter the coordinates of point 2 (x2, y2): ').split())
x3, y3 = map(float, input('Enter the coordinates of point 3 (x3, y3): ').split())

# Calculate the lengths of the sides
side1 = pow((pow((x2 - x1), 2) + pow((y2 - y1), 2)), 2)
side2 = pow((pow((x3 - x2), 2) + pow((y3 - y2), 2)), 2)
side3 = pow((pow((x1 - x3), 2) + pow((y1 - y3), 2)), 2)

# Calculate semi-perimeter
s = (side1 + side2 + side3) / 2

# Calculate area using Heron's formula
area = pow((s * ((s - side1) * (s - side2) * (s - side3))), 2)


print('The area of the triangle is:', area)