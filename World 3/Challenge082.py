value = list()
odd = list()
even = list() 
while True:
    value.append(int(input('Type a number: ')))
    answer = str(input('Do you want to proceed? [Y/N] ')).strip().upper()[0]
    if answer in 'Nn':
        break
print(f'The full list of number typed is {value}')
for n in range(0, len(value)):
    if value[n] % 2 == 0:
        odd.append(value[n])
    else:
        even.append(value[n])
print(f'The odd numbers list is {odd}')
print(f'The even numbers list is {even}')
