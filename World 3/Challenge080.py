value = []
for count in range(0,5):
    num = (int(input('Type a number: ')))
    if count == 0 or num > value[-1]:
          value.append(num)
          print('Added to the end of the list...')
    else:
        position = 0
        while position < len(value):
            if num <= value[position]:
                value.insert(position, num)
                print(f'Added to the position {position}...')
                break
            position += 1
print(f'The values typed in order are {value}')      
