word = str(input('Type one phrase or expression: ')) .strip().upper()
phrase = word.split()
text = ''.join(phrase)
reverse = ''
for l in range (len (text)-1, -1, -1):
    reverse += text [l]
if reverse == text:
    print('Yes, is a palindrome!')
else:
    print('NO, is not a palindrome!')
