from random import sample
from time import sleep
lottery = list()
print('-='*30)
print('***EURO MILIONS***')
print('-='*30)
num = int(input('How many play do you want draw? '))
for c in range(num):
    d = sorted(sample(range(1, 61),6))
    lottery.append(d[:])
    print(f'Draw {c + 1}:{d}')
    sleep(1)
print('-=' *5, ' < GOOD LUCK! >', '-=' * 5)
