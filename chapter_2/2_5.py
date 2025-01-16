money = eval(input('Enter The Subtotal: '))
gratuity = eval(input('Enter The Gratuity: '))

actual_gratuity = gratuity / 100
ratio = money * actual_gratuity
subtotal = money + ratio

print('The Gratuity is', ratio, 'and The Total is', subtotal)