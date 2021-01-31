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
maxi=0
k=d.values() # gets all values in dictionary.
m=max(k)
for i,j in d.items(): # opens ups the key, values as items like list of tuples[(key,value)]. But not tuple.
    if j==m:
        nme=i
        val=j
print(f'{nme} {val}')
# simplified using tuples too is in files3_simplified.py
