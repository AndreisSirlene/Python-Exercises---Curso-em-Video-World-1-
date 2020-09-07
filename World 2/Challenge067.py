num = 0
count = 0
print('--'*20)
while True:
    num = int(input('Type a number to see their TABLE: '))
    print('--'*20)
    if num < 0:
        break
    for count in range(1, 11):
        print(f'{num} x {count} = {num*count}')
print('Negative number END the program!!!')
   