import base

while True:
    answer = base.menu (['Check Registered profiles', 'Register People', 'Exit System'])
    if answer == 1:
        base.title('Option 1')
    elif answer == 2:
        base.title('Option 2')  
    elif answer == 3:
        base.title('Living the system... Bye!')
        break
    else:
        print('ERROR: please type a valid option!')
    print()