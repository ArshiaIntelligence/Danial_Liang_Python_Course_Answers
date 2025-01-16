weight = float(input('Enter weight in pounds: '))
height = float(input('Enter height in inches: '))

weight_kg = weight * 0.45359237
height_m = height * 0.0254
bmi = weight_kg / pow(height_m, 2)

print('BMI is',bmi)