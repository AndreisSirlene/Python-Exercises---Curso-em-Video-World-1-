def increase(n = 0, p = 0):
    result = n + (n * p / 100)
    return result
   

def decrease(n = 0, p = 0):
    result = n - (n * p / 100)
    return result
    


def double(n = 0):
    result = n * 2
    return result
 

def half(n = 0):
    result = n / 2
    return result


def coin(n, coin = '€'):
    return f'{coin}{n:.2f}'.replace('.',',')
