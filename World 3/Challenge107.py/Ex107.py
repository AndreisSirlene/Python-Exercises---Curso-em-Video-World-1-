import coin

n = float(input('Type a price: $ '))
print(f'By increase 15% we have a new price of {coin.increase(n, 15)}')
print(f'Half of {n} is {coin.half(n)}')
print(f'Double of {n} is {coin.double(n)}')
print(f'By decrease 12%, we have a new price of {coin.decrease(n, 12)}')
