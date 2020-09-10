num = tuple(int(input('Type a number: ')) for c in range (4))
print(f'The numbers typed are: {num}') 
print(f'The number 9 appears {num.count(9)} times.')
if 3 in num:
    print(f'The first number 3 was typed in the position {num.index(3)+1}.')
else:
    print(f'The number 3 does not appear in the sequence typed.')
print('The ODD number(s) typed in the sequence are ',end=' ')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
