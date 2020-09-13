name = list()
weight = list()
while True:
    name.append(str(input('Name: ')))
    weight.append(int(input('Weight: ')))
    answer = str(input('Do you want to proceed? [Y/N]: ')).strip().upper()[0]
    if answer in 'Nn':
        break
print(f'In total was registered {len(name)} people.')
print(f'The most havy weight is {max(weight)}Kg, which is the weight of ',end='')
for c in range(0, len(weight)):
    if weight[c] == max(weight):
        print(f'[{name[c]}]')
print()
print(f'The most light weight is {min(weight)}Kg, which is the weight of ',end='')
for c in range(0, len(weight)):
    if weight [c] == min(weight):
        print(f'[{name[c]}]')
