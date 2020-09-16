game = dict()
data = list()
total = 0
game ['name'] = str(input('Name of player: ')).strip().upper()
total = int(input(f'How many games {game["name"]} had play? '))
for c in range (0, total):
    data.append(int(input(f'How many goals na partida {c+1}? ')))
game['goals'] = data[:]
game['Total'] = sum(data)
data.append(game.copy())
print('-='*20)
print(game)
print('-='*20)
for k, v in game.items():      
    print(f'The space {k} has the value {v}.')
print('-='*20)
print(f'The player {game["name"]} play {total} games.')
for i, v in enumerate (game['goals']):
    print(f'In the game {i +1}, made {v} goals')

