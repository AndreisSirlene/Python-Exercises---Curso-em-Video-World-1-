d= int(input('How many days rented? '))
k= int(input('How many Km drived? '))
t= (d*60)+(k*0.15)
print('The total to pay is R${:.0f}.'.format(t))
