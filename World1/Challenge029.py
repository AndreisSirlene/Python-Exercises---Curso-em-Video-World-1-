k = int(input('What is the speed of your car in Km/h right now? '))
t = (k-80)*5
if t>80:
    print('\033[0;30;41mYou excced the limit speed of 80Km in this road. You have a fine of ${}\033[m '.format(t))   
else:
    print('You are under limited speed, well done!')

