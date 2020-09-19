
from time import sleep
def count(start, end, inter):
    print()
    print('◄►'*20)
    print(f'- Count from {start} to {end} in {inter} in {inter}.')
    if inter < 0:
        inter *= -1
    if inter ==0:
        inter = 1
    if start <= end:
        for c in range(start, end + inter, inter):
            sleep(0.3)
            print(c, end=' → ' if c < end else '\n')
    else:
        for c in range (start, (end - inter), -inter):
            sleep(0.3)
            print(c, end =' → ' if end < c else'\n')

# Main Program

count(1,10,1)
count(10,0,2)
print('◄►'*20)
print('Now is your turn to decide the score! ')
start = int(input('Start: '))
end = int(input('End: '))
inter = int(input('Interval: '))
count(start, end, inter)
print()
print('PROGRAM END ')