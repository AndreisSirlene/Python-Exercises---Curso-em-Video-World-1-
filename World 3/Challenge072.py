num = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eigth','nine',
'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
'eighteen', 'nineteen', 'twenty')
answer = ' '
while True:
    while True:
        option = int(input('Type a number between 0 and 20: '))
        if 0 <= option <= 20:
            break
        print('Option Invalid! ', end= ' ')
    print(f'You typed the number {num[option]}.')
    print(' ')
    answer = str(input('Do you want to proceed? [Y/N] ')).strip().upper()[0]
    if answer =='N':
        break
print('End')    
    