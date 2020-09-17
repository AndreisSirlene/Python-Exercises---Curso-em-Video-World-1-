game = dict()
players = list()
data = list()
while True:
    game.clear()
    game ['name'] = str(input('Name of player: ')).strip().upper()
    total = int(input(f'How many games {game["name"]} had play? '))
    data.clear()
    for c in range (0, total):
        data.append(int(input(f'How many goals na partida {c+1}? ')))
    game['goals'] = data[:]
    game['Total'] = sum(data)
    players.append(game.copy())
    answer = str(input('Do you want to proceed?[Y/N] ')).upper().strip()[0]
    while answer not in 'YN':
        print('ERROR! Please type Y or N')
        answer = str(input('Do you want to proceed?[Y/N] ')).upper().strip()[0]
    if answer == 'N':
        break
print('◄►'*25)
print('''Cod   NAME        GOALS       TOTAL 
----------------------------------------------------''')
for k, v in enumerate(players):
    print(f'{k:>3}  ', end='' )
    for d in v.values():
        print(f'{str(d):<13}  ',end='')
    print()
print('◄►'*25)
while True:
    search = int(input('Which player do you want see the goals?(99 stop program)'))
    if search == 99:
        break
    if search >= len(players):
        print(f'Error! Player {search} does not exist.')
    else:
        print(f' -- Analyse of PLAYER {players[search] ["name"]}:')
        for i, g in enumerate (players[search]['goals']):
            print(f'In the game {i+1}, made {g} goals')
    print('◄►'*25)