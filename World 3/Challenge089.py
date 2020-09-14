student = list ()
average = list()
note = list()
answer = 'yYnN'
while True:
    student.append(str(input('Name: ')))
    note.append(float(input('Grage 1: ')))
    note.append(float(input('Grade 2: ')))
    answer = str(input('Do you want to proceed? [Y/N]: ')).strip().upper()[0]
    student.append(note[:])
    student.append((note[0]+ note[1])/2)
    average.append(student[:])
    student.clear()
    note.clear()
    if answer in 'nN':
        break
print('◄►'*15)
print(f'{"AVERAGE GRADES":^30}')
print('◄►'*15)
print('''Nº       NAME           AVERAGE 
-------------------------------------''')
for i, student in enumerate(average):
    print(f'{i}       {average[i][0]:<15} {average[i][2]}')
print('-------------------------------------')
while True:
    check = int(input('Which student do you want see the grades?(999 end program): '))
    if check == 999:
        break
        print('Program END')
    if check <= len(average)-1:
        print(f'The grades of {average[check][0]} are {average[check][1]}')
print('-----WELCOME BACK-----')
