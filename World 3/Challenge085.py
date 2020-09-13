number = [[], []]
num = 0
for c in range (1, 8):
    num = int(input('Type a number: '))
    if num % 2 == 0:
        number[0].append(num)
    else:
        number[1].append(num)
print(f'All the number typed are: {number} ')
print(f'The odd numbers typed are:{sorted(number[0])}')
print(f' The even numbers typed are: {sorted(number[1])}')
      