# Looping through links within links to get specific name in a link
import urllib.request, urllib.response, urllib.error, urllib.parse
import ssl
import re
from bs4 import BeautifulSoup

cert=ssl.create_default_context()
cert.check_hostname=False
cert.verify_mode=ssl.CERT_NONE

count=0
url='http://py4e-data.dr-chuck.net/known_by_Seatle.html'
while count<7:
    rd=urllib.request.urlopen(url, context=cert).read()
    html_parser=BeautifulSoup(rd,'html.parser')
    tags=html_parser('a')
    tag_pos=0
    for tag in tags:
        tag_pos+=1
        if tag_pos==18:
            url=tag.get('href')
            break
    count+=1
print(url)
print((url.split('_')[2]).split('.')[0])



