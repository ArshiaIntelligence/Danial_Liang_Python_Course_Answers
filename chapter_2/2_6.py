from random import randint

number = randint(0, 1000)
sum_of_digits = 0

while number > 0:
    sum_of_digits += number % 10
    number //= 10

print('The sum of the digits is:', sum_of_digits)


# randint = به ما اجازه میدهد که از بین بازه اعداد درخواستی یک عدد به صورت رندوم بیرون بکشیم