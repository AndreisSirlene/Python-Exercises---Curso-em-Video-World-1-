print('=='*20)
print('Terms of Aritmetic Progression')
print('=='*20)
num = int(input('First Term: '))
reason = int(input('Reason: '))
term = num
count = 1
total = 0
num1 = 10
while num1 != 0:
    total = total + num1
    while count <= total:
        print('{} ¬ '.format(term),end=' ')
        term += reason
        count += 1   
    print('Pause!')
    num1 = int(input('Do you want see more terms? How many: '))
print('End')
