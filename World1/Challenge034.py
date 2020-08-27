w = float(input('Tell me your current earns: '))
i = (w *0.10) + w
s = (w * 0.15) + w
if w > 1250:
    print('As your wage is already over $1250.00, from now you will receive a increase of 10% which brings the total earn to ${:.2f}.'.format(i))
else:
    print('As your wage is under $1250.00, from now you will receive a increase of 15% which ends up in a total of {:.2f}'.format(s))
