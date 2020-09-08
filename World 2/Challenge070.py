print('==*=='*8)
print('       SHOP LIST')
print('==*=='*8)
totalcost = float(0)
lowerp = int(10000000000)
bestp = str('')
count = int(0)
while True:
    namep = str(input('Type a name of a product: ')).upper()
    costp = float(input('How much cost:$'))
    totalcost += costp
    if costp > 1000:
        count += 1
    if costp < lowerp:
        lowerp = costp
        bestp = namep
    answer = str(input('Do you want proceed [Y/N]? ')).strip().upper()[0]
    if answer == 'N':
        break
print(f'In total you expende ${totalcost}, from that {count} product cost above $1000.')
print(f'And the more afordable product is a {bestp}')
