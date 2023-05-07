# XML BASICS 
# XML Schema 
# skipped this topic 

# JSON 

import json 
data = '''{
"name" : "utkarsh", 
"email": {
"hide": "yes"
}
}'''

info = json.loads(data) 
print("Name", info["name"]) 
print("Hide", info["email"]["hide"]) 

# service oriented approach 

