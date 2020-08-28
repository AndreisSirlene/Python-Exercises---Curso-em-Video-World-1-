import math
num = int(input('Type any number in any size: '))
print('''Now, can you please choose below in which conversion base you want to see:
[1] Binary 
[2] Octal 
[3] Hexadecimal''')
c = int(input('Your choice is: '))
#used below the technique that allow slice the strings, so just show the relevant part, as Python 
if c==1:
    print('{} converted to binary is equal to {}'.format(num, bin(num)[2:]))
elif c==2:
    print('{} converted to Octal is equal to {}'.format(num, oct(num)[2:]))
elif c==3:
    print('{} converted to Hexadecimal is equal to {}'.format(num, hex (num)[:2]))
else:
    print('Invalid option, sorry!')