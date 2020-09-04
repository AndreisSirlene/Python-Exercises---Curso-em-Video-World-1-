'''The challenge is to ask the gender of a person (in this case I only used Male and Female) in case 
the user type another answer the program should keep running and ask for a valid answer'''
gender = str(input('What is your gender? [F/M]: ')).upper().strip()[0]
while gender not in 'MmFf':
    gender = str(input('Value does not match. What is your gender[F/M]: ')).strip().upper()
print('{} Genger sucessful registered!'.format(gender))
