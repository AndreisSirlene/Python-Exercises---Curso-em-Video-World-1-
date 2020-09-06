'''Create a program that read many numbers, and stop if the user type 999.
At the end show how many numbers were typed and the total sum, excluding the (999). 
Basically recomend use of WHILE '''
num = 1
count = 0
sum = 0
while num != 999:
    num = int(input('Type a number [Will stop if type 999]: '))
    if num != 900:
        count += 1
        sum = sum + num
print('You have typed {} number(s) and the sum of all is {}.'.format(count, sum))
		