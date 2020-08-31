p = str(input('Type a product that you need to buy: '))
p1 = float(input('Please, tell how much is costing to buy {} today: $'.format(p)))
print('''Select how do you want to pay:
[1] Cash 
[2] Card
[3] Card Split 2x 
[4] Card Split 3x or more ''')
c = int(input('What is your preference? '))
if c==1:
    print('By paying in Cash the {} will cost ${:.2f}'.format(p, p1 - (p1*0.10)))
elif c==2:
    print('By paying in card the {} will cost ${:.2f}' .format(p, p1 - (p1*0.05)))
elif c==3:
    print('By paying in card split 2X the {} wil cost ${:.2f}'.format(p, p1))
    if c==3:
        print('Each parcel will cost ${:.2f}'.format(p1/2))
elif c==4:
    totalp = int(input('How many parcels?'))
    e = p1 + (p1*0.20)
    pm = e/totalp
    print('By paying in card split in {} parcels the {} wil cost ${:.2f} in total with interest.'.format(totalp, p, e))
    print('Each parcel will cost ${:.2f}'.format(pm))
else:
    print('OPTION NOT AVAILABLE')

