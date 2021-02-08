import re
text = '''
This is a test String [more or less]
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
hvvgADFHBasfhbASRTSKJnFSiN

Hello
ssp.gmail.com

32.47.09.sp sp
(123<321(9)])
Meta characters to be escaped
. ^ $ * + ? { } [ ] | ( ) \
Mr.sandy
Mr.dany
'''
# to find a pattern and its index
ind=re.compile(r'gmail') # compiles the patter that we are searching for
itering=ind.finditer(text) # Iterating through the text to match our compiled pattern and creates iterable object
for txt in itering: # iterating through object
    print(txt) # returns the match and its index in span
print(text[130:135])

# word boundary
wb=re.compile(r'\bsp') # compiles the patter that we are searching for. we check for sp after non alpha-numeric val
wb_iter=wb.finditer(text) # Iterating through the text to match our compiled pattern and creates iterable object
for word in wb_iter: # iterating through object
    print(word) # returns two matches. sp next to dot and next to space
print(text[150:152])

wB=re.compile(r'\Bsp') # compiles the patter that we are searching for. we check for sp after alpha-numeric val
wB_iter=wB.finditer(text) # Iterating through the text to match our compiled pattern and creates iterable object
for word in wB_iter: # iterating through object
    print(word) # returns one. sp next to s.
print(text[127:129])

# start and end
st=re.compile(r'^\nThis')
start=st.finditer(text)
for s in start:
    print(s)
print(text[0:5].split()) # splitting the new line.

en=re.compile(r'dany\n$')
end=en.finditer(text)
for e in end:
    print(e)
print(text[238:242])