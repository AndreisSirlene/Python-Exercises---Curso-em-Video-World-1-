r = 0
print('=='*15)
print('10 Terms of PA')
print('=='*15)
t = int(input('First Term: '))
r = int(input('Reason: '))
p = t + (11-1) * r
for c in range (t, p, r):
        print((c),end=' * ')
print('END')
    