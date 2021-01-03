# casefold()-> returns everything as lowercase.
# lower()->same as above.
# upper()-> returns in uppercase.
# count()-> returns the occurrences count in string.
print("Welcome to L0v3 metric!")
name_1=input("Enter your name:")
name_2=input("Enter their name:")
n1=[]
n2=[]
for t in "true":
    n1.append(name_1.casefold().count(t))
for l in "love":
    n2.append(name_2.casefold().count(l))
print(f'Yours love metric is {str(sum(n1))+str(sum(n2))}%')