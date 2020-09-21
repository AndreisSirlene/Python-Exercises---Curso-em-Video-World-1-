def leiaInt(txt):
    n = input(txt)
    while not n.isnumeric():
        print('ERROR! Type a valid interger.')
        n = input(txt)
    option = int(n)
    return option 

#main program
n = leiaInt('Type a number: ')
print(f'You just typed the number {n}.')
