'''PLAY CHALLENGE! Create a game where the computer choose a number betweem 0 and 20, the user need try to guess 
the number picked by a computer, the program also need to count how many times the user try until answer correctly'''
num = ''
import random
computer = random.randint(0,20)
print('==*=='*20)
print('I am a faster machine, already choose my number between 0 and 20! Try to bit me!')
print('==*=='*20)
num = int(input('Your number now: '))
count = 1
while num != computer:
    if num > computer:
        print('Try small number: ')
    elif num < computer:
        print('Infomr a high number: ')
    num = int(input('Try again: '))
    count += 1
print('After try {} times the user win!'.format(count))
