n = str(input('Type your full name: ')).strip()
name = n.split()
print('My first name is {}'.format(name[0]))
print('My last name is {}'.format(name[len(name)-1]))