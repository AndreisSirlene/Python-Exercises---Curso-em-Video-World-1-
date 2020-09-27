import base

while True:
    answer = base.menu (['Check Registered People', 'Register People', 'Exit System'])
    if answer == 1:
        base.title('REGISTERED PEOPLE')
        base.see()

    elif answer == 2:
        base.title('NEW REGISTER')
        base.register()
    elif answer == 3:
        base.title('Leaving the system... Bye!')
        break
    else:
        print('ERROR: please type a valid option!')
    print()
    