def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERROR: Please, type one interger valid number.\033[m')
            continue
        except KeyboardInterrupt:
            print('The user prefer not inform the data.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            nf = float(input(msg)).real
        except (ValueError, TypeError):
            print('Please type a Real number.')
            continue
        except KeyboardInterrupt:
            print('The user prefer not inform the data.')
            return 0
        else:
            return nf


#main program
n = leiaInt('Type a INTERGER number: ')
print(f'The number typed was {n}')
nf = leiaFloat('Type a REAL number: ')
print(f'The Real number typed was {nf}')
     