sum = 0
n = int(input('Type any number: '))
for c in range(2, n):
    if n % c == 0:
        sum = sum + 1
    else:
        sum = sum
if sum == 0:
    print('The number {} is considered a PRIME NUMBER'.format(n))
else:
    print('The number {} is NOT a PRIME number'.format(n))
