value = []
for count in range(0, 5):
    value.append(int(input('Type a number: ')))
print(value)
print(f'The higher value is {max(value)} and is in the position(s) ',end='')
for i, v in enumerate(value):
    if v == max(value):
        print(f'{i}...',end='')
print()
print(f'The lower value is {min(value)} and is in the position(s)',end='')
for i, v in enumerate(value):
    if v == min(value):
        print(f'{i}...',end='')