# \n newline character 
# \n newline is one character 
# open() method 

fhand = open("sample.txt", "r")
print(fhand)

stuff = "Hello\nworld!" # output Hello (nextline) world
print(stuff)

# reading files with for loop 
xfile = open("sample.txt")
print(xfile)
for cheese in xfile:
    print(cheese)

# counting the number of lines in a file 
fhand = open("sample.txt") 
count = 0 
for line in fhand:
    count = count + 1
print("line count is", count)

# reading the whole file with read() method 

fhand = open("sample.txt")
inp = fhand.read() 
print(len(inp))
print(inp)

# searching through a File 
fhand = open("sample.txt")
for line in fhand:
   print(":-",line.startswith("line"))
   if(line.startswith("line")):
       print("found")

print("--------------------------------")
# removig gap while print lines of a file 
fhand = open("sample.txt")
for line in fhand:
    line = line.rstrip()
    print(line) 

# not() operator 
# continue 

fhand = open("sample.txt")
for line in fhand:
    line = line.rstrip()
    if not "@uct.ac.za" in line:
        continue
    print(line) 


#Prompt input() method  quit() method
fname = input("Enter the file name:")
try:
    fhand = open(fname)
except:
    print(fname, "cannot be opened")
    quit()
count = 0
for line in fhand:
    count = count + 1
print("There were", count, "lines in the selected file") 

 




