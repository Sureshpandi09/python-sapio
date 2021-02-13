#  Parsing json with multiple key:value pairs in list
import json
text='''[
{ "Name":"SP",
  "Contact":{ 
            "phone":"987654321",
            "type":"intl"
            },
  "email":{ 
          "hide":"yes"
           }
},
{ "Name":"elon",
  "Contact":{ 
            "phone":"123456789",
            "type":"intl"
            },
  "email":{ 
          "hide":"no"
           }
}
]'''
json_dic=json.loads(text) # return list of dic. Because it is having the value as such
print(type(json_dic))
print(len(json_dic)) # 2 as there are two key:value pair
for dic in json_dic:
    print(dic["Name"])
    print(dic["Contact"]["phone"])
    print(10*'*')
