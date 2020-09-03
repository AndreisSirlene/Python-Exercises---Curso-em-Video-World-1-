highValue = 0
lowValue = 0
for person in range(1, 6):
    weight = float(input('What is the weight of {}ª person: '.format(person)))
    highValue = highValue if highValue != 0 and hv > weight else weight
    lowValue = lowValue if lowValue != 0 and lowValue < weight else weight
print('The person with high weight has {:.2f}Kg and with lower weight has {:.2f}Kg.'.format(highValue, lowValue))
