from datetime import date
a = date.today().year
y = int(input('Which year you was born? '))
i= a-y
print('According to the information provide you are {} years old in 2020'.format(i))
if i<=16:
    print('You still have time to signing for militar career.')
elif 16<=i<=18:
    print('You are in the right time to enter a militar career in Brazil')
elif i>=19:
    print('You are in deficit with your militar obligation.')
