import emoji
import time
print('Lets count together for the end of 2020.')
for c in range (10, 0, -1):
    time.sleep(1)
    print(c)
print(emoji.emojize('Happy New Year!!!:fireworks:', use_aliases = True))
