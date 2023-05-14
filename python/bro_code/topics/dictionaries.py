# js(objects) 
capitals = {
    "India": "New Delhi", 
    "USA": "Washington DC"
}
# print(capitals["Germany"]) # error germany not exists in the dict
print(capitals.get("Germany")) # not throw error 
print(capitals.keys())
print(capitals.values()) 
print(capitals.items()) # list of object with key value pair 

for key,value in capitals.items():
    print("Key",key,"value", value) 

capitals.update({"Germany": "Berlin"})  
# can also update existing keys 
capitals.update({"India":"Delhi"}) 

print(capitals)

# rmv a key value 
capitals.pop("Germany")
print(capitals) 

# clears everything from dict
capitals.clear()
print(capitals)

