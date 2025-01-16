number = input("Enter your digit integer: ")

if number.isdigit():
    reversed_number = number[::-1]
    print("The number in reverse order is:", reversed_number)
else:
    print("Please enter a valid digit integer.")