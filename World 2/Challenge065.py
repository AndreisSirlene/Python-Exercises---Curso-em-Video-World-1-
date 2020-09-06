'''Create a program that read many numbers, and at the end shows the average of the values, 
which was the higest number and lower one. Also ask if the user want keep typing.'''
highNum = lowNum = sum = count = average = 0
answer ='Y'
while answer == 'Y':
    num = int(input('Type a number: '))
    answer = str(input('Do you want keep typing?[Y/N]: ')).strip().upper()
    highNum = highNum if highNum != 0 and highNum > num else num
    lowNum = lowNum if lowNum != 0 and lowNum < num else num 
    sum += num
    count += 1
    average = sum/count
print('You typed {} numbers, their average is {} with high number {} and lower {}.'.format(count, average, highNum, lowNum))
