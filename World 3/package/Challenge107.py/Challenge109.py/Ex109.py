import coin

n = float(input('Type a price: '))
print
print(f'By increase 15% we have {coin.increase((n), 15, True)}')
print(f'Half of {coin.coin(n)} is {coin.half(n, True)}')
print(f'Double of {coin.coin(n)} is {coin.double(n, True)}')
print(f'By decrease 12% we have {coin.decrease((n), 12, True)}')