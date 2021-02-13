# Every HTTP(S) request/response will be  done as data.
# Wire Protocol -> when we run a code that connects to other system/server via internet, it will be sent as serialised data and the receiving end system will deserialize it.
# xml and json are most used formats by all codes.
# xml schema -> every end point system will have a schema and will accept the xml request only if the xml is in that schema.
# xml validator -> xml document + xml schema
import xml.etree.ElementTree as ET
xml_data='''<person>   
                <name>SP</name>
                <phone type="intl">9876543210</phone> 
                <email hide="yes"/>   
            </person>'''
tree=ET.fromstring(xml_data) # returns an object by parsing the xml passed. We passed string that is in xml format
print(tree.find('name').text) # getting value of the key(tag)
print(tree.find('phone').text)
print(tree.find('phone').get('type')) # getting attribute's value of the key
print(tree.find('email').get('hide'))
