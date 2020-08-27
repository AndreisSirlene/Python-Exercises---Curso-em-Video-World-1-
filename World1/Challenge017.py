from math import hypot 
co= float(input('Define a value of the Opposite side of a triangle: '))
ca= float(input('Define a value for the adjacent side: '))
print('The hypotenuse length is:{:.2f} '.format(hypot(co,ca)))