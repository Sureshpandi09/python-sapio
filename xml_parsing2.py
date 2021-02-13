# Reading xml from url and parsing its value and getting sum of the value in count element.
import urllib.request, urllib.response, urllib.error
import xml.etree.ElementTree as ET
url='http://py4e-data.dr-chuck.net/comments_1014716.xml'
read_url=urllib.request.urlopen(url)
xml_str=''
for line in read_url:
    line=line.decode().strip()
    xml_str+=line+'\n'
xml_str=xml_str.rstrip()
tree=ET.fromstring(xml_str)
tree_list=tree.findall('comments/comment')
count=0
for element in tree_list:
    val=int(element.find('count').text)
    count+=val
print(count)
