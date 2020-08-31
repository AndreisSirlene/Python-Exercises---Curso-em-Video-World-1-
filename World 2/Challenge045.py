import math
#other option is import randint directly:
#from random import randint
print('{:=^40}'.format(' JOKENPO '))
print('''Lets play! Your options: 
[0] STONE
[1] PAPER
[2] SCISSOR''')
p = int(input('What is your Choice? '))
print('''JO
KEN
PO!!!''')
import random
c = random.randint(0,2)
itens = ('STONE', 'PAPER','SCISSOR')
print('-='*15)
print('''Computer choose {} 
Player choose {} '''.format(itens [c], itens [p]))
print('-='*15)
if c == 0:
    if p == 0:
        print('TIE')
    elif p == 1:
        print('PLAYER WIN')
    elif p == 2:
        print('COMPUTER WIN')
elif c == 1:
    if p == 0:
        print('COMPUTER WIN')
    if p == 1:
        print('TIE')
    if p == 2:
        print('PLAYER WIN')
elif c == 2:
    if p == 0:
        print('PLAYER WIN')
    if p == 1:
        print('COMPUTER WIN')
    if p == 2:
        print('TIE')
