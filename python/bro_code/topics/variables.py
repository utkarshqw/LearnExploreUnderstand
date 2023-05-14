# string 
# integer 
# float 
# boolean
# multiple assignmnets

name = "Goku"
print(name) 
print("Hello" + name)
print(type(name))

first_name = "Naruto"
last_name = "Uzumaki" 
full_name = first_name + " " + last_name

print("Hello",full_name )

age = 21 
age = age+1
age += 1
print(age) 
print(type(age))
# print("your age is" + age) this will throw error but js will not 
#bu we can use str() to convert number to string 
print("Your age is: " + str(age))

# int is whole number 
# float is decimal number 

height = 250.5 
print("Your height is: "+str(height) + "cm")
print(type(height)) # float 

# boolen 
human = False 
print(human) 
print(type(human)) # bool type 
print("Are you a human? " + str(human)) 

name = "Bro"
age = 21 
young = True 

print(name)
print(age)
print(young) 

# now let's do it with multiple assignments 

name, age, young = "Goku", 47, True 

print(name)
print(age)
print(young) 

# if all values are equal 

spongebob = patrick = sandy = squidward = 30 
print(spongebob)
print(patrick)
print(sandy)
print(squidward)








