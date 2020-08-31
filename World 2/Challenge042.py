n1 = float(input('Type one value: '))
n2 = float(input('Type a second value: '))
n3 = float(input(' Type another value: '))

print('Now I have the 3 values, we can confirm if they form a triangle and which type is!')
if (n1+n2 < n3) or (n2+n3 < n1) or (n3+n1 < n2):
    print('It is not a Triangle')
elif (n1==n2) and (n2==n3):
    print('It is an EQUILATERAL triangle!')
elif (n1==n2) or (n1==n3) or (n2==n3):
    print('It is an ISOSCELES triangle!')
else:
    print('It is an ESCALENE triangule!')



#Three sides creat a triangule when the sum of any two sides is bigger then the third side.
#Equilateral Triangle: three sides are equal;
#Isosceles Triangle: any two sides are equal; 
#Escalene Triangle: three sides are different;

# #Another way to code this problem as suggested in the clase is:
# n1 = float(input('Type one value: '))
# n2 = float(input('Type a second value: '))
# n3 = float(input(' Type another value: '))
# if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
#     print('The values above create a TRIANGLE ',end='')
#     if n1==n2==n3:
#         print('Equilateral')
#     if n1 != n2 != n3 != n1:
#         print('Escalene')
#     else:
#         print('Isosceles')
# else:
#     print('The values above does not create a TRIANGLE')