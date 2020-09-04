num1 = int(input('Type a number: '))
num2 = int(input('Type a second number: '))
option = 0
while option != 5:
    print('[1] SUM \n[2] MULTIPLY \n[3] HIGHER \n[4] NEW NUMBERS \n[5] LEFT PROGRAM')
    option = int(input('>>>>> What is your choice: '))
    if option == 1:
        print('The sum of {} and {} is a total of {}.'.format(num1, num2, (num1 + num2)))
    elif option == 2:
        print('By multiplication {} times {} will result in a total of {}.'.format(num1, num2, (num1*num2)))
    elif option == 3:
        print('The next number after {} and {} in sequence is {} and {}.'.format(num1, num2, (num1+1), (num2+1)))
    elif option == 4:
        print('>>> Inform other numbers >>> ')
        num1 = int(input('Type first number: '))
        num2 = int(input('Type a second number: '))
    elif option == 5:
        print('Live the Program')
    else:
        print('Option Invalid! Try another.')
    print('=*='*20)

