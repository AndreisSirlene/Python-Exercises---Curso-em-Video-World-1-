print('==+==+==+== POET1C BANK ==+==+==+==')
value = int(input('How much do you want to withdraw?$ '))
amount = value
note = 100
totalnote = 0
while True:
    if amount >= note:
        amount -= note
        totalnote += 1
    else:
        if totalnote > 0:
            print(f'Total of {totalnote} note(s) of ${note}.')
        if note == 100:
            note = 50
        elif note == 50:
            note = 20
        elif note == 20:
            note = 10
        elif note == 10:
            note = 5
        totalnote = 0
        if amount == 0:
            break
print('Thank you for your PREFERENCE!')
