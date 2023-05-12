# function = a block of code which is executed only when it is called

def hello():
    print("hello!") 
    print("have a nice day")

hello()
hello()
hello()

#arguments 

def hello(name):
    print("hello!" + name) 
    print("have a nice day")

hello("Dude")

# sending variables as arg
name = "Bro"
hello(name)

def hello(first_name, last_name, age):
    print("hello"+first_name+" "+last_name)
    print("You are "+str(age)+ " years old") 
    print("Have a nice day!")
hello("Bro", "Code", 21)
