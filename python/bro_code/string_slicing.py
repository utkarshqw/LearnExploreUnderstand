# indexing[] or slice()
# [start:stop:step] 

name = "Naruto Uzumaki"

# getting first name from name 
first_name = name[0:6] # exclusive 6
# first_name = name[:6] first value assumed 0 
print(first_name) 

last_name = name[7:] 
last_name = name[7:14] 
print(last_name)

#using third argument step
funky_name = name[0:14:2] # take every 2nd character
funky_name = name[::2] # same as above 
print(funky_name)

# we can also reverse a string with the help of negative value of steps 
reversed_name = name[::-1] 
print(reversed_name)

# slice function 

website = "http://google.com" 
website2 = "http://wikipedia.com" 
slice = slice(7, -4  ) 
print(website[slice]) 
print(website2[slice]) 




