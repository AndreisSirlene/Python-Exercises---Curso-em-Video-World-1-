matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
odd = sum = higher = 0
for h in range (0, 3): 
    for v in range (0, 3):
        matriz[h][v] =int(input(f'Type a value for position [{h}, {v}]:'))     
for h in range (0, 3):  
    for v in range (0, 3):
        print(f'[{matriz[h][v]:^5}]',end='')
        if matriz[h][v] % 2 == 0:
            odd += matriz[h][v]
    print()
print('-='*30)
print(f'The sum of the odd numbers from the matriz are: {odd}.')
print('-='*30)
for v in range(0, 3):
    sum += matriz[v][2]
print(f'The sum of the third column of matriz is {sum}.')
print('-='*30)
for h in range(0,3):
    if h == 0:
        higher = matriz[1][h]
    elif matriz[1][h] > higher:
        higher = matriz[1][h]
print(f'The higher number in the second line is {higher}.')
print('-='*30)