num = sum = count = 0
while True:
    num = int(input('Type a number [Program will stop with 999]: '))
    if num == 999:
        break
    sum += num
    count += 1
print(f'In total was typed {count} numbers and their sum is in total {sum}.')
        