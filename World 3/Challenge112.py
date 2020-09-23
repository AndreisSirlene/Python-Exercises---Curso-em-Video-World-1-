try:
    a = int(input('Numerator: '))
    b = int(input('Denominator: '))
    r = a / b
except (ValueError, TypeError):    # creat a variable to treat the exception
    print(f'The problem is with type of data that you inform.')
except ZeroDivisionError:
    print('Is not possible to divide a number per zero!')
except KeyboardInterrupt:
    print('The user prefer not inform the data.')
else:
    print(f'The result is {r:.1f}')
finally:
    print('You are welcome back any time!')