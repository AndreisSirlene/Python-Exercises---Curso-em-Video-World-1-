n1 = int(input('Type the first number:'))
n2 = int(input('Type the second number of your choice:'))
n3 = int(input('Type the third number that comes in your mind right now: '))
print('\033[1;33mI will help you to identify the smallest and largest number now!\033[m')
#To define the smallest number
smallest = n1
if n2 < n1 and n2 < n3:
    smallest = n2
if n3 < n1 and n3 < n2:
    smallest = n3
#To define the largest number
largest = n1
if n2 > n1 and n2 > n3:
    largest = n2
if n3 > n1 and n3 > n2:
    largest = n3
print('\033[1;31;46mThe smallest number defined is: {} \033[m'.format(smallest))
print('\033[7;40mThe largest number you defined is: {} \033[m '.format(largest))
