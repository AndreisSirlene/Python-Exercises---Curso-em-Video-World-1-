import random
from time import sleep
c = random.randint(0,10)
print('_-_'*40)
print('I am thinking in a number between 0 and 20. Try to bit me!/n ') #this is the computer acting
print('_-_'*40)
p = int(input('The number I picked is: ')) #This is the player acting
print('Processing...')
sleep(2)
if p==c:
    print('\033[1;30;40mYou Win!!!\033[m')
else:
    print('\033[4;31mSorry, I choose number {}. Good Look next time!!!\033[m'.format(c))


