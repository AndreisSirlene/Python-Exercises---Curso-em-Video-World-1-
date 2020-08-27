phrase = str(input('Type any phrase:')).upper().strip()
print('In this phrase the letter I appears {} times'.format(phrase.count('I')))
print('The first letter I appears in the position {}'.format(phrase.find('I')+1)) 
print('The last position that letter I appears is {}'.format(phrase.rfind('I')+1))