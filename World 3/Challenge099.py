def higher(*num):
    size = len(num)
    h = max(num)
    print(f'By analysing the values inputed... \n{num} Was informed {size} values in total.')
    print(f'The highest value informed was {h}.')
def lin():
    print('~'*50)

#Main Program
lin()
higher(8, 3, 2, 9, 0, 13, 4)
lin()
higher(7, 0, 5, 1)
lin()
higher(6, 3, 7, 1, 8, 2)
lin()
higher(4)
lin()
