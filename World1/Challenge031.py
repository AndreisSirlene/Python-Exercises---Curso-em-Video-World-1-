print('=*='*45)
d = float(input('What is the distance to travel from Dublin to Letterkenny in km? '))
t = d*0.5
r = d*0.45
print('=*='*45)
if d<=200:
    print('To travel from Dublin to Letterkenny the ticket will cost \033[1;31;46m${:.2f}\033[m'.format(t))
else:
    print('\033[1mTo travel from Dublin to Letterkenny the ticket will cost \033[7;33m${:.2f}\033[m as exceed 200 km.\033[m'.format(r))

    