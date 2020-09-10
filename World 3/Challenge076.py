#To show the shop list in a table style, I considered that all name of products are in Odd position
#  and their values in Even position, so apply the if % 2 == 0'''
shop = ('Bread', 1 , 'Milke', 1.60, 'Donuts', 0.70, 'Chicken', 3, 'Nutella', 2.5, 'Cheese', 1.40,'Orange', 0.80, 'Prawns', 4, 'Tomato Sause', 2)
print ('*=*'*15)
print('          PRICE LIST')
print ('*=*'*15)
for item in range(0, len(shop)):
    if item % 2 == 0:
        print(f'{shop[item]:.<30}',end='')
    else:
        print(f'€{shop[item]:>7.2f}')
