# Using API provided by coursera which can be accessed for free for the assignment to get the place id of location by API and parsing that json
import urllib.request, urllib.response, urllib.parse
import ssl
import json

# creating default context for ssl with no certificate
cert=ssl.create_default_context()
cert.check_hostname=False
cert.verify_mode=ssl.CERT_NONE

chuck_API='http://py4e-data.dr-chuck.net/json?'
details=input('Enter location: ')
# Each key:value passed to the urlencode() will be added as new parameter(separated by &) to the url query
url=chuck_API+urllib.parse.urlencode({'address':details,'key':42})
print(url) # http://py4e-data.dr-chuck.net/json?address=PUCMM&key=42
url_read=urllib.request.urlopen(url, context=cert).read()
url_toString=url_read.decode() # decoding bytes(url content) will return string.
js=json.loads(url_toString)
print(json.dumps(js, indent=4)) # will return the values of js with indentation of 4spaces(tab) for  easy reading
place=js['results'][0]['place_id']
print(f'Place id {place}')

# import urllib.request, urllib.response, urllib.parse
# import json
# geocode API format -> https://maps.googleapis.com/maps/api/geocode/outputFormat?parameters
# geoAPI='https://maps.googleapis.com/maps/api/geocode/json?'
# details='SP, Thelichathanallur, Paramakudi'
# url=geoAPI+urllib.parse.urlencode({'address':details})
# print(url) https://maps.googleapis.com/maps/api/geocode/json?address=SP%2CThelichathanallur%2CParamakudi
# url_read=urllib.request.urlopen(url).read()
# print(type(url_read))
# issue in accessing geocode api. And the API seems to be billable to use





