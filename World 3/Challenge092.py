file = dict()
data = list()
from datetime import date
file ['name'] = str(input('Name: '))
file ['age'] = date.today().year - int(input('Year of Birth: '))
file ['pps'] = str(input('PPSn (If no PPS informe 0): '))
if file ['pps'] != 0:
    file ['register'] = int(input('Year of PPS register: '))
    file ['wage'] = float(input('Wage: €'))
    file ['retirement'] = file ['age'] + ((file ['register'] + 35) - date.today().year)
data.append(file.copy())   
print(file) 
for e in data:
    for k, v in e.items():
        print(f' - {k} has value {v} ')
    