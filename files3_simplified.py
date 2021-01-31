# To get person who sent maximum mail using dictionary and list
file_path = "D:\\DS\\test.txt"
fl = open(file_path)
lst = list()
d=dict()
nme=''
val=''
for line in fl:
    if line.startswith("From:"):
        names=line.strip().split()[1]
        lst.append(names)
for name in lst:
    # <dict>.get() -> gets the value of key(name). If no value, a new input for the key(name) with value 0 will be set in the dictionary.
    d[name]=d.get(name,0)+1
l=[]
for k,v in d.items():
    l.append((v,k))# appending (key,value) as tuples as (value,key) to sort using values.
sort_ed=sorted(l,reverse=True)# sorting with values and reverse is true to get it in descending order.
print(f'{sort_ed[0][1]} {sort_ed[0][0]}')



