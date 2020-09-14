student = dict()
student['name'] = str(input('Name: '))
student ['grade'] = float(input(f'{student["name"]} Final Grade: '))
if student ['grade'] >= 7:
    print('_ Situation is Approved!')
elif 5 <= student['grade'] < 7:
    print('_ Situation in dependence!')
else:
    print('_ Situation is reproved!')
for k, v in student.items():
    print(f'_ {k} is equal to {v}')
print()