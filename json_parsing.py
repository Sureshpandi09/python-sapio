# json -> simplest data interchange format. It will be like key:value pair in python dictionary.
import json
text='''{ "Name":"SP",
  "Contact":{ 
            "phone":"987654321",
            "type":"intl"
            },
  "email":{ 
          "hide":"yes"
           }
}'''
# loads -> load from string
json_dic=json.loads(text) # will return parsed json as python dictionary. Thus can be accessed as dictionaries.
print(json_dic)
print(type(json_dic))
print(json_dic["Name"])
