# **kwargs  parameter that will pack all arguments into a dictionary 
# useful tso that a function can accept a vering amount of keyword argument

def hello(first, last):
    print("Hello", first + " " + last) 

# hello(first="Bro", middle="last", last="code") # this will throw error because we have only first and last as arguments 
# To solve this we can use **kwargs 


def hello(**kwargs):
    print("Hello" + kwargs["first"] + " " + kwargs["last"])
    print("Hello", end=" ") 
    for key,value in kwargs.items():
        print(value, end=" ") 




   
hello(title="Mr.",first="Bro", middle="Dude", last="Code")

