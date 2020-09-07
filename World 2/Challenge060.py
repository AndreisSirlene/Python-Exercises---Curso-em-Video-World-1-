'''This option was code using de module:
from math import factorial
num = int(input('Type a number: '))
f = factorial (num)
print('The factorial of {} is {}.'.format(num, f))'''
num =  int(input('Type a number to find out his factorial: '))
count = num
factorial = 1
print('Factorial {}! = '.format(num),end=' ')
while count > 0:
    print('{}'.format(count),end=' ')
    factorial *= count
    count -= 1
    print('x' if count >=1 else'=',end= ' ')   
print('{}.'.format(factorial))