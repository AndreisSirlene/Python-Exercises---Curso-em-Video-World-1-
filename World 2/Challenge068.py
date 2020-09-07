from random import randint
w = 0
print('=*='*20)
print('LET IS PLAY ODD or EVEN')
print('=*='*20)
while True:
    num = int(input('Type your number [0 to 10]: '))
    computer = randint(0,10)
    total = computer + num
    play = ' '
    while play not in 'EO':
        play = str(input('ODD or EVEN? [O/E]: ')).upper().strip()
    print(f'You play {num} and computer {computer}. Total of {total} is ',end='')
    print('ODD' if total % 2 == 0 else 'EVEN')
    if play == 'O':
        if total % 2 == 0:
            print('You WIN!!!')
            w += 1
        else:
            print('You LOST!')
            break
    elif play == 'E':
        if total % 2 == 1:
            print('You WIN!!!')
            w += 1
        else:
            print('You LOST!')
            break
    print('Let is play Again...')
print(f'GAME OVER! You have won {w} time(s).')
