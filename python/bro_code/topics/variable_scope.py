# scope = The region that a variable is recognized 
# a variable is only availble from inside the region it is created. 
# a global and locally scoped version of a variable can be created 

name = "Bro"
def display_name():
    name = "Code"
    print(name) 

# print(name) error name is not defined because name variable is not in our scope here
display_name()
print(name)

# python follows #LEGB convention 
# L = local 
# E = Enclosing 
# G = Global 
# B = Built-in 


