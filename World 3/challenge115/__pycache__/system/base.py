def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERROR:please type a valid option.')
            continue
        except KeyboardInterrupt:
            print('The user prefer not inform the data.')
            return 0
        else:
            return n


def line():
    print('-'*40)
    

def title(txt):
    line()
    print(txt.center(40))
    line()


def menu(lista):   
    title('MAIN MENU')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    line()
    opc = leiaInt('Your option: ')
    return opc
