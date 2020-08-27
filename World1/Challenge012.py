p=int(input('The price of the product is: '))
n=(p - (p * 5/ 100))
print('The new price of the product after a offer of 5 percent of discount is going to be ${:.1f}.'.format(n))