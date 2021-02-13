# function to read data from url and getting integers in the line having <span>
import urllib.request, urllib.response # library to fetch data from web with sockets enabled within.
import re
url='http://py4e-data.dr-chuck.net/comments_1014714.html'
rd=urllib.request.urlopen(url) # returns value in http response.
# rd=urllib.request.urlopen(url).read()-> returns bytes
num=0
for line in rd:
# iterating each content of http response will return bytes. Iterating through bytes will return int.
# decode() applicable for bytes class only.
    line=line.decode().strip()
    if 'span' in line:
        num+=(int(''.join(re.findall('[0-9]+', line)))) # regex to find all numbers in a line of string
print(num)