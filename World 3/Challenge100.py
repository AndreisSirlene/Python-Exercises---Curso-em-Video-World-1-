from random import randint
def shufle(lista):
    print(f'Drawing 5 values from the list: ',end='') 
    for count in range(0, 5):
        n = randint(0, 50)
        lista.append(n)
        print(f'{n} ',end='')
    print()
     

def sumOdd(lista):
    s = 0
    for value in lista:
        if value % 2 == 0:
            s += value          
    print(f'Adding up the Odd values from {lista}, we got {s}.')
  
number = list()
shufle(number)
sumOdd(number) 



