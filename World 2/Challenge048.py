s = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
             s += n
print('The sum of the ODD numbers that are multiple of 3 betweem 1 and 500 is {}.'.format(s))
