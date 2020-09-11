value = list()
answer = ' '
while True:
    value.append(int(input('Type a number: ')))
    answer = str(input('Do you want to proceed? [Y/N] ')).strip().upper()[0]
    if answer in 'Nn':
        break
print(f'In total was typed {len(value)} numbers.')
value.sort(reverse = True)
print(f'The list typed in reverse order is {value}')
if 5 in value:
    print('Number 5 was typed in the list.')
else:
    print('Number 5 was not found in the list')
