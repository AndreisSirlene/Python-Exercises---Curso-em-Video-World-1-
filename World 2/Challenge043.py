w = float(input('What is your weight? (Kg) '))
h = float(input('What is your height? (m) '))
bmi = w / (h**2)
print('The BMI of this person is {:.1f}'.format(bmi))
if bmi < 18.5:
    print('Becarful you are under weight!')
elif 18.5 <= bmi < 25:
    print('Congratulations, your weight is ideal!')
elif 25  <= bmi <= 30:
    print('You are overheight')
elif 30 <= bmi <= 40:
    print('You are in obesity')
else:
    print('Morbity Obesity')
    