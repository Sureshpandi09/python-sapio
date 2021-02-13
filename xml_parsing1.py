# Parsing xml with multiple tags
# serialisation -> The act of taking data stored in a program and formatting it so it can be sent across the network. 
# JSON and XML -> most used data-interchange format
# complex elements -> elements with ore than one child element(tags)
# no need of indentation in xml. Its just for our convenient.
import xml.etree.ElementTree as ET
xml_data='''<details>
            <persons> 
                <person> 
                    <name>SP</name>
                    <phone type="intl">9876543210</phone> 
                    <email hide="yes"/>
                </person>
                <person>
                    <name>Elon</name>
                    <phone type="intl">123456789</phone> 
                    <email hide="nope"/>
                </person>
          </persons>
          </details>'''
tree=ET.fromstring(xml_data)
# tree_list=tree.findall('details/persons/person') # need to check why it is returning from child tag only.
# print(tree_list)
# print(len(tree_list)) returns 0
tree_list=tree.findall('persons/person')
print(tree)
print(tree_list)
print(f'Len :{len(tree_list)}, type:{type(tree_list)}')
for branch in tree_list:
    print(branch.find('name').text)
    print(branch.find('phone').text)
    print(branch.find('email').get('hide'))
    print(10*'*')
