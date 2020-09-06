'''calculate a Aritmetic progression and show the first term and reason. 
The idea is to use 'While'''
print('=='*20)
print('10 Terms of Aritmetic Progression')
print('=='*20)
num = int(input('First Term: '))
reason = int(input('Reason: '))
term = num
count = 1
while count <= 10:
    print('{} ¬ '.format(term),end= '')
    count += 1
    term += reason
print('End Program')