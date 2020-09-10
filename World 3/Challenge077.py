
'''The challenge is to identify the voguel in a list of words inside a tuple.'''
words = ('hamburguer', 'juice', 'pizza', 'dessert','fries', 'beer', 'pint', 'hot dog', 'chocolate', 'wine')
for w in words:
    print(f'\nIn the word {w.upper()} has ',end='')
    for letter in w:
        if letter.lower () in 'aeiou':
            print(letter, end=' ')
