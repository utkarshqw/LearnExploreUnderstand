# index operator [] gives access to a dequence's element (str, list, tuples) 

name = "bro Code!"

if(name[0].islower()):
    name = name.capitalize()

print(name)   

# Range
first_name = name[:3].upper() 
last_name = name[4:].lower() 

print(first_name)
print(last_name) 

#negative indexing 
last_character = name[-1]
print(last_character) 

