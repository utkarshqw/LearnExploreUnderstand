# with open("read_file.txt") as file:
    # print(file.read()) 
# after the above code the file will automatically close

# print(file.closed)    

# chatGPT code from line 7-18
# Open the file in read mode
file = open('read_file.txt', 'r')

# Read the contents of the file
contents = file.read()

# Close the file
file.close()

# Print the contents of the file
print(contents)

try:
    with open("read_file.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(") 

  


