# List comprehension, Sorting examples. Tuples can be compared. If tuple contains strings, each letter of string will be compared until it gets 'True' or 'False'.
file_path = "D:\\DS\\test.txt"
fl = open(file_path)
lst = list()
d=dict()
for line in fl:
    if line.startswith("From "):
        names=line.strip().split()[5].split(':')
        lst.append(names)
hours=[h[0] for h in lst]
for k in hours:
    d[k]=d.get(k,0)+1
lst_vk=[(key,value) for key,value in d.items()]
out=sorted(lst_vk)
for i,j in out:
    print(f'{i} {j}')