# import the library re
import re
path='D:\\DS\\find_sum_regex.txt'
fl=open(path)
lst=[]
for line in fl:
    if line.isspace():
        continue
    if re.search('[0-9]',line): # returns True if pattern matches in the line passed
        lst_val = re.findall('[0-9]+', line) # returns list of values in the provided pattern
        print(lst_val)
        for i in lst_val:
            i=int(i)
            lst.append(i)
            break
print(f'There are {len(lst)} values with sum={sum(lst)}')
# read about Greedy and Non-greedy matching using regex.