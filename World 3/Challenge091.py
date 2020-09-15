from random import randint
from time import sleep
dice = dict()
data = list()
print(' >>> DICE ROLL <<< ')
for i in range(1, 5):
    data.append(randint(1, 6))
for i in range (0, 4):
    dice[f'player {i + 1}'] = data[i]
for k, v in dice.items():
    print(f'The {k} got {v} ')
    sleep(1)
print('◄►'*15)
print('Ranking of Players:')
c = 1
for k in sorted(dice, key = dice.get, reverse=True):
    print(f'{c} position: {k} with {dice[k]} points')
    c += 1