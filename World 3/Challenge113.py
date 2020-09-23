def leiaInt(txt):
    n = input(txt)
    while not n.isnumeric():
        print('Type a interger number: ')
        n = (txt)
    option = int(n)
    return option
        

def leiaFloat(msg):
    nf = input(msg)
    while not nf.isalpha():
        print('Type a real number: ')
        nf = (msg)
    option = int(nf)
    return option


#main program
while True:
    try:
        n = leiaInt('Type a interger number: ')
        nf = leiaFloat('Type a Real number: ')
        break
    except ValueError:
        print('ERROR: Please, type one interger valid number.')
    except KeyboardInterrupt:
        print('The user prefer not inform the data.')
    else:
        print('The interger value is {n} and the real was {nf} ')