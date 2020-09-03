from datetime import date
now = date.today().year
totalab = 0
totallo = 0
for p in range (1, 8):
    born = int(input('In which year the {}ª  person was born? '.format(p))) 
    age = now - born
    if age >= 21:
        totalab += 1
    else:
        totallo += 1
print('In total {} people are in maiority age and {} are under 21 years old.'.format(totalab, totallo))
     