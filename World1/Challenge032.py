year = int(input('Type a year to verify if was a Leap year: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: 
    print('Yes!{} is a leap year.'.format(year))
else:
    print('No, {} is not a leap year.'.format(year))