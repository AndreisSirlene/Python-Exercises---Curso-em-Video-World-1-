n = int(input('Type a number betweem 0 and 9999: '))
print('The number {} is split as show bellow:'.format(n))
u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10
print('The unity is {}.'.format(u))
print('The ten is {}.'.format(d))
print('The hundred is {}.'.format(c))
print('The thousand is {}.'.format(m))