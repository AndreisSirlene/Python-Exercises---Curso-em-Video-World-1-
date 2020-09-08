
print('***'*10)
print('      PROFILE')
print('***'*10)
total = tmale = female20 = 0
while True:
    age = int(input('AGE: '))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('GENDER [M/F]:')).strip().upper()[0]
        if age >= 18:
            total += 1
        if gender == 'M':
            tmale += 1
        if gender == 'F'  and age < 20:
            female20 += 1
    ask = ' '
    while ask not in 'YN':
        ask = str(input('Do you want to proceed? [Y/N]: ')).upper().strip()[0]
    if ask == 'N':
        break
print(f'From all profiles registered {total} are over 18 years old.')
print(f'{tmale} are men, and {female20} are women under 20 years.' )
print('End')
       