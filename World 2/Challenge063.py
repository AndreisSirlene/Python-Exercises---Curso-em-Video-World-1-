num = int(input('Type how many numbers of the Fibonacci sequence you want to see: '))
f1 = 1
f2 = 0
count = 1
print('{} ->'.format(f2),end=' ')
while count != num:
    print('{} ->'.format(f1),end= ' ')
    f1 += f2
    f2 = f1 - f2
    count += 1
print('End') 
