'''from random import sample
num = tuple(sample(range(20),5))
print(num)
print(f'The higher value is {max(num)} and the lower is {min(num)}.')'''

from random import randint
num = (randint(0,20), randint(0,20), randint(0,20), randint(0,20), randint(0,20))
print ('The shuffle values are: ',end=' ')
for n in num:
    print(f'{n} ',end=' ')
print(f'\nThe higher value is {max(num)} and the lower is {min(num)}.')