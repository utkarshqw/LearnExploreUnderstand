student = ("Bro", 21, "male") 
# How many times Bro appear in the tuple student
print(student.count("Bro"))

# index of a element 
print(student.index("male")) 

for x in student:
    print(x)

if "Bro" in student: 
    print("Bro is here")

# tuples cannot be changed 