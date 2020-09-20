def factorial(num, show=False):
    f = 1
    if show == True:
        for c in range(num, 1, -1):
            f *= c
            print(f'{c} x ',end='')
        print(f'1 = ',end='')
        return f
    if show == False:
        for c in range(num, 1, -1):
            f *= c
        return f'The factorial of {num} is {f}'


#Main Program
n = int(input('Type a number to show the factorial: '))
show = input('Do you want details?[Y/N] ').strip().upper()[0]
while show not in 'YN':
    show = input('Do you prefer see the details? [Y/N]: ').upper()[0]
if show in 'Yy':
    show = True
else:
    show = False
print(factorial(n, show))
