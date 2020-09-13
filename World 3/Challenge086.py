matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for h in range (0, 3):   #this first two for are used to input data
    for v in range (0, 3):
        matriz[h][v] =int(input(f'Type a value for position [{h}, {v}]:'))     
for h in range (0, 3):   #this for are for show the structure
    for v in range (0, 3):
        print(f'[{matriz[h][v]:^5}]',end='')
    print()