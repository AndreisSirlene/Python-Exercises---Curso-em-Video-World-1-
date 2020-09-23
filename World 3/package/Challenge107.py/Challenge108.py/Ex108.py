import coin

n = float(input('Type a price: € '))
print(f'By increase 15%, we have a new price of {coin.coin(coin.increase((n), 15))}')
print(f'Half of {coin.coin(n)} is {coin.coin(coin.half(n))}')
print(f'Double of {coin.coin(n)} is {coin.coin(coin.double(n))}')
print(f'By decrease 12%, we have a new price of {coin.coin(coin.decrease((n), 12))}')
