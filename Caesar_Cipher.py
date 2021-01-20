print('Welcome!!!')
inp=input('Please type E to Encrypt or D to Decrypt: ')
char=[]
for i in range(0,26):
    char+=chr(97+i)
# print(char)
temp=[]
if inp == 'E' or inp == 'D':
    if inp == 'E':
        txt=input('Type your message:\n').lower()
        key=int(input('Please provide the key to encrypt: '))
        for j in txt:
            temp.append(char.index(j))
        temp=[val+key for val in temp]
        print(temp)
        print(char.index('z'))
        for t in temp:
            if t>char.index('z'):
                temp[temp.index(t)]=t%26
        print(temp)
        enc=[char[x] for x in temp]
        print(f'Your encrypted text: {"".join(enc)}')
    else:
        txt = input('Type your message:\n')
        key = int(input('Please provide the key to decrypt: '))
        for j in txt:
            temp.append(char.index(j))
        temp = [val-key for val in temp]
        dec = [char[x] for x in temp]
        print(f'Your decrypted text: {"".join(dec)}')
else:
    print("Please provide valid input and try")