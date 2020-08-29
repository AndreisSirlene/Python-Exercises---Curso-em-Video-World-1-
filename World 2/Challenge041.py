from datetime import date
d = date.today().year
y = float(input('Type the year you was born: '))
#r= age range
r = d - y
if r <= 9:
    print('By the Swimming Federation you are classified as category LITTLE')
elif  14 >= r > 9:
    print('By the Swimming Federation you are classified as category CHILD')
elif 19 >= r > 14:
    print('By the Swimming Federation you are classified as category JUNIOR')
elif 20 >= r >19:
    print('By the Swimming Federation you are classified as category SENIOR')
else:
    print('By the Swimming Federation you are classified as MASTER')
