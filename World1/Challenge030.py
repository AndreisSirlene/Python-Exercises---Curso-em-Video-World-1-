#town = 'Letterkenny'
#colors = {'blackandwhite':'\033[7;30m',
#'blue':'\033[1;34m',
#'yellow':'\033[0;33m',
#'clear':'\033[m'}
#print('Welcome to {}{}{}! Enjoy your stay with us!'.format(colors['blue'], town, colors['clear']))


n = int(input('Type a number:\033[1;31m'))
if (n % 2) == 0:
    print('\033[4;33m{0} is a Even Number\033[m'.format(n))
else:
    print('\033[4;36m{0} is a Odd Number\033[m'.format(n))