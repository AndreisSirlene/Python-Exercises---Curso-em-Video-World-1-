highAge = 0
sumAge = 0
people = [''] * 4
gender = [''] 
age = ['']
oldName = ''
totalWoman20 = 0
for p in range (1,5):
    print('==*=='*10)
    people = str(input('What is the name of the {}ª person: '.format(p))).strip().upper()
    age = int(input('What is the age of the {}ª person: '.format(p)))
    gender = str(input('What is the gender of the {}ª person (M/F): '.format(p))).strip()
    print('==*==' *10)
    sumAge += age
    if p == 1 and gender in'Mm':
        highAge = age
        oldName = people
    if gender in 'Mm' and age > highAge:
        highAge = age
        oldName = people 
    if gender in 'Ff' and age < 20:
        totalWoman20 += 1
average = sumAge / 4 
print('The average age of the group is {} years.'.format(average))
print('The old MALE has {} years old and his name is {}.'.format(highAge, oldName))
print('In the whole group there is {} women age under 20.'.format(totalWoman20))