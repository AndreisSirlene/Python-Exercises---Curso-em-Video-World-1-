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


def see():
    while True:
        try:
            file = open('profile.txt', 'r')  # open is a internal function of the python program
            txt = file.read()
            for profile in txt:
                print(profile, end='')
            file.close()
            break
        except FileNotFoundError:
            print('File do not exist\nBut was created!')
            file = open('profile.txt','w+')
            file.close()
            break
        return file

def register():
    file = open('profile.txt','a')
    while True:
        try:
            name = str(input('Name: ')).upper().strip()
            age = int(input('Age: '))
        except:
            print('Type a valid value')
        else:
            file.write(f'{name:<20}{age:>15} anos')
            file.write('\n')
            file.close()
            break

