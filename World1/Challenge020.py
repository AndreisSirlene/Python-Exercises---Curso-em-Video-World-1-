import random
s1= str(input('Student number one is: '))
s2= str(input('Student number two is: '))
s3= str(input('Student number three is: '))
s4= str(input('Student number four is: '))
list=[s1,s2,s3,s4]
random.shuffle(list)
print('The order of presentation is as follow: ')
print(list)
