# str.format()  optional method that gives users more control when displaying output 

animal = "cow" 
item = "moon" 

print("The " + animal + " jumped over the " + item)

print("The {} jumped over the {}".format(animal, item)) 
# positional argument
print("The {1} jumped over the {0}".format(animal, item)) 
#with keyword
print("The {animal} jumped over the {item}".format(animal="lion", item="river")) 
print("The {animal} jumped over the {animal}".format(animal="lion", item="river")) 

# more better way of doing the above things 
text = "The {} jumped over the {}" 
print(text.format(animal, item)) 

name = "Bro" 
print("Hello, my name is {}".format(name)) 
#provide padding to strings
print("Hello, my name is {:10}. Nice to meet you".format(name)) 
print("Hello, my name is {:<10}. Nice to meet you".format(name)) 
print("Hello, my name is {:>10}. Nice to meet you".format(name)) 

# to center name between the padding
print("Hello, my name is {:^10}. Nice to meet you".format(name)) 

# print only upto 2 decimal places 
number = 3.14159
print("The number pi is {:.2f}".format(number)) 

number = 1000
print("comma at thousand place {:,}".format(number)) 
print("number binary form is {:b}".format(number)) 
print("octo number {:o}".format(number)) 
print("Hexa decimal {:X} and {:x}".format(number, number)) # capital x and X for capital and small 
print("Scientific notation {:E}".format(number)) # same as above capital and small E





