# input() function 
name = input("What is your name ? ")
print("Hello "+ name) 

age = input("How old are you: ") 
# user input is always of str type 
# here we have converted to int but what if someone provided float value 
age = int(age) + 1 # we count have also put input() inside the int()
print("You are " + str(age) + " years old.") 

# for float input 
height = float(input("How tall are you? ")) 
print("You are " + str(height) + " cm tall") 









