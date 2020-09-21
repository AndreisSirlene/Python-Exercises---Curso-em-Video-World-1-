c = ('\033[m',   # 0 - no color      # C variable is a global variable
     '\033[0;30;41m', # 1 - red
     '\033[0;30;42m', # 2 - green
     '\033[0;30;43m', #3 - yellow
     '\033[0;30;44m', # 4 - blue
     '\033[0;30;45m', # 5 - purple
     '\033[0;30m'     # 6 - white
)


def helping(com):
    text(f'Accessing the command guide \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def text(msg, color=0):
    size = len(msg)+3
    print(c[color], end='') #start with color here
    print('~'*size)
    print(f'  {msg}')
    print('~'*size)
    print(c[0], end='') ##here clean the previous color


#main program
command = ''
while True:
    text('Help System PyHELP',  2)
    command = str(input('Function or Library > '))
    if command.upper() == 'END':
        break
    else:
        helping(command)
text('Good Job!',  1)
