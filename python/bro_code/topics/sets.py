# set = collection which is unordered, unindexed. No dulicate values 
#  even if we write duplicate values it will only show unique values
utensils = {"fork", "spoon", "knife", "knife","knife"} 
dished = {"bowl", "plate", "cup"} 
for x in utensils: 
    print(x)
utensils.add("napkin")    
utensils.remove("fork")
utensils.clear() 

# add all the data inside utensils set to dishes set 
dishes.update(utensils) 

for x in dishes:
    print(x)

# json two sets together and create a new set entirely 

dinner_table = utensils.union(dishes) # or vice-versa

# things that one set has but not the other
print(utensils.difference(dishes)) # or vice-versa 

