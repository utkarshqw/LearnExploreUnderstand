# input method
# name = input("Enter:")
# print(name)

# length of string 
# print(len(name))

# looping through string 

fruit = "banana"
for letter in fruit:
    print(letter)


# Intermediate Strings 

# slicing strings 

str = "Monty Pyton"
print(str[0:4]) # not including 4 
print(str[:2]) # assumes 0 as beginning 
print(str[8:]) # assumes last index as beginning 

# concatination with + 

# using in as a logical Operator 

fruit = "banana" 
print("n" in fruit )
print("m" in fruit) 
print("nan" in fruit) 
if "a" in fruit:
    print("a is present in banana") 

# lowcase and uppercase letters 
print(max("a","A")) # res: "a" 

# lower() string method 
greet = "Hello Bob" 
zap = greet.lower() 
print(zap)

#type operator 
print(type(greet))

# print(dir(greet))  # all the methods for string 

# string methods look 
# .find() method to find index

fruit = "banana"
pos = fruit.find("z")
pos = fruit.find("na")
print(pos)

# search and replace 
# replace() method 

greet = "Hello Bob"
nstr = greet.replace("Bob","Utkarsh") # whereever it will find bob will replace it with utkarsh whether found once or more than once 
print(greet)
print(nstr)

# trim the whitespace 
# lstrip() rstring() strip()

greet = "  Hello Bob    "
greet.lstrip()
greet.rstrip()
greet.strip()

#Prefixed 
# str.startswith()

print(greet.startswith("  H")) 











