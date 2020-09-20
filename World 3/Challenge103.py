def token(name, goals):
    if not name:
        name = '<unknown>'
    if not goals or not goals.isnumeric():
        goals = 0
    print(f'The player {name} made {goals} goal(s) in the championship.')

#main program
token(str(input('Name of Player: ')).strip().upper(), str(input('How many goals in the championship? ')).strip())
