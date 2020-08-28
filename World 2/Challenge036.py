from time import sleep
h = float(input('How much will cost your new house? '))
w = float(input('What is your monthly wage?' ))
y = int(input('How many years you pretend to pay back the house?' ))
tm = h / (y*12)
Limite = w * 0.30
print('You are considering pay a house worth ${:.2f} in a period of {} years, with a salary of ${:.2f}. Let have a look if we can aprove your Loan.'.format(h,y,w))
print('PROCESSING...')
sleep(3)
if (w * 0.30) >= tm:
    print('Loan APPROVED!!! Congratulations!')
elif tm <= tm:
    print('Infortunatly your Loan is NOT APPROVED!')
    