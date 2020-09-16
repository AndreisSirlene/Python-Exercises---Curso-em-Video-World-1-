file = dict()
group = list()
answer = ''
totalAge = count = 0
while True:
    file ['name'] = str(input('Name: '))
    file ['gender'] = str(input('Gender [F/M]: ')).strip().upper()[0]
    file ['age'] = int(input('Age: '))
    totalAge += file ['age']
    group.append(file.copy())
    file.clear()
    count += 1
    answer = str(input('Do you want to proceed? [Y/N] ')).strip().upper()[0]
    if answer in 'Nn':
        break
average = totalAge / count
print('-='*35)
print(group) 
print('-='*35) 
print(f'A) In total was registered {count} people.')
print(f'B) The average age of the group is {average}.') 
print(f'C) The woman registered are: ')
for p in group:
    if p['gender'] in'fF':
        print(end='')
        print(p['name'])
print(f'D) People with age above average: ')
for p in group:
    if p['age'] > average:
        for k, v in p.items():
            print(f' {k} = {v};',end='')
