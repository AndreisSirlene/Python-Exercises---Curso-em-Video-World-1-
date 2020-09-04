
# Python program to find the factorial of a number provided by the user
factorial = 1
num = int(input('Type a number : '))
while factorial != 0:
    if num < 0:
        print('Sorry, factorial does not exist for negative numbers')
    elif num == 0:
        print('The factorial of 0 is 1')
