value = list()
answer = ' '
while True:
    num = int(input('Type a number: '))
    if num not in value:
        value.append(num)
        print('Value added Successfully!')
    else:
        print('The value already typed! Try another!')
    answer = str(input('Do you want to proceed? [Y/N]:')).strip().upper()[0]
    if answer in 'Nn':
        break
value.sort()
print(f'The numbers typed in crescent order are {value}')
    