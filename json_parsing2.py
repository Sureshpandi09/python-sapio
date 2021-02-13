# Reading json from url and parsing its value and getting sum of the value in count element.
import urllib.request, urllib.response, urllib.error
import json
url='http://py4e-data.dr-chuck.net/comments_1014717.json'
read_url=urllib.request.urlopen(url).read().decode() # returns string
js=json.loads(read_url)
print(js['comments'])
val=0
for dic in js['comments']:
    val+=dic['count']
print(val)


