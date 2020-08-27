print('We have a mission to find out if the length of 3 diferent sides can be defined as a triangle, please tipe values for a, b and c')
a = float(input('Length A: '))
b = float(input('Length B: '))
c = float(input('Length C: '))

if  b-c < a < b + c and a-c < b < a + c and a-b < c < a + b:
    print('The sides of A, B and C can shape a triangle.')
else:
    print('The sides os A, B and C put together does not create a triangle.')

