def coin(n = 0, coin = '€'):
    return f'{coin}{n:.2f}'.replace('.',',')


def increase(n = 0, i = 0, formato=False):
    result = n + (n * i / 100)
    return result if formato is False else coin(result)
   

def decrease(n = 0, d = 0, formato=False):
    result = n - (n * d / 100)
    return result if formato is False else coin(result)
    


def double(n = 0, formato=False):
    result = n * 2
    return result if formato is False else coin(result)
 

def half(n = 0, formato=False):
    result = n / 2
    return result if format is False else coin(result)

def resume(n = 0, i = 0, d = 0):
    print('~'*40)
    print('RESUME OF VALUE'.center(30))
    print('~'*40)
    print(f'Value analysed: \t\t{coin(n)}')
    print(f'{i}% of inscrease is:\t\t{increase(n, i, True)}')
    print(f'Half of the value is:\t\t{half(n, True)}')
    print(f'Double of the value is:\t\t{double(n, True)}')  #'\t' is universal tabulation
    print(f'{d}% of decrease is:\t\t{decrease(n, d, True)}')
    print('~'*40)