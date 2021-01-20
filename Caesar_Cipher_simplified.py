############################# CIPHER FUNCTION ##########################################################
print("Welcome to cipher function")
char = []
for i in range(0, 26):
    char += chr(97 + i)
inp = input('Please type E to Encrypt or D to Decrypt: ')
if inp == 'E':
    inp = 'encrypt'
elif inp == 'D':
    inp = 'decrypt'
else:
    print("Please provide valid input")
    exit()
txt = input('Type your message:\n')
key = int(input('Please provide the key to shift: '))


def cipher(text=txt, shift=key, action=inp):
    temp = []
    for j in text:
        temp.append(char.index(j))
        if action == 'D':
            shift *= -1
        temp = [val + shift for val in temp]
        for t in temp:
            if t > char.index('z'):
                temp[temp.index(t)] = t%26
        msg = [char[x] for x in temp]
        print(f'Your {action}ed text: {"".join(msg)}')


cipher('hello',5,'E')
