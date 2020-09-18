
from time import sleep
def count(start, end, inter):
    print()
    print(f'_Count from {start} to {end} in {inter} in {inter}.')
    if start <= end:
        for c in range(start, end + inter, inter):
            sleep(0.3)
            print(c, end=' → ' if c < end else '\n')
        else:
            for c in range (start, (end - inter), -inter):
                sleep(0.3)
                print(c, end =' → ' if end < c else'\n')
print('◄►'*25)
# Main Program

count(1,10,1)
count(10,0,2)
print('Now is your turn to decide the score! ')
start = int(input('Start: '))
end = int(input('End: '))
inter = int(input('Interval: '))
count(start, end, inter)
print()
