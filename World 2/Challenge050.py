s = 0
count = 0
for c in range (1,7):
    n = int(input('Type a number: '))
    if n % 2 == 0:
        s += n
        count += 1
print('The sum of {} ODD numbers is {}'.format(count, s))