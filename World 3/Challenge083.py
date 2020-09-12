list1 = []
list2 = []
equation = input('Type a math equation: ')
for c in equation:
    if c == '(':
        list1.append(c)
    elif c == ')':
        list2.append(c)
if len(list1) == len(list2):
    print('The expression is right!')
else:
    print('Expression not correct!')