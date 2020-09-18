#area function
def area(w, l):
    a = w * l
    print(f'The area of the land {w} x {l} is {a}m²')

def line(txt):
    print(txt)
    print('='*25)
#main program
line(' Defining Land Area ')
w = float(input('WIDTH (m): '))
l = float(input('LENGTH (m): '))
area(w, l)


    
