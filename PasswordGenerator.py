import random # to use shuffle() and choice() methods
print("Welcome to Password generator!!!")
total_letters=int(input('How many characters would you like in your password?\nEnter in range of 0 to 14: '))
capital_alpha=[] # list of capital letters
small_alpha=[] # list of small letters
for i in range(0,26):
    capital_alpha.append(chr(65+i))
# print(capital_alpha)
for m in range(0,26):
    small_alpha.append(chr(97+m))
# print(small_alpha)
char=capital_alpha+small_alpha
n=[l for l in range(0,10)] # list of numbers 0-9
# print(n)
s=['!','@','#','$','%','^','&','*','?','/','\\']
password=[]
if 0 < total_letters <= 14:
    numbers = int(input('How many numbers would you like?\n'))
    if numbers<total_letters:
        symbols = int(input('How many symbols would you like?\n'))
        if numbers+symbols<=total_letters:
            for i in range(0,numbers):
                password.append(str((random.choice(n))))# join() does not support int.
            for j in range(0,symbols):
                password.append(random.choice(s))
            for k in range(0,total_letters-(numbers+symbols)):
                password.append(random.choice(char))
            print(f'Password before shuffle: {password}')
            random.shuffle(password)
            print(f'Password after shuffle: {password}')
            # joining elements in list to single string.
            print(f'Your real password: {"".join(password)}')
        else:
            print('No space for symbols in the password')
    else:
        print('Please provide valid input')
else:
    print('Please provide value in the mentioned range')
