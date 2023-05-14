import os 

# source = "move_file.txt" 
source = "folder" 
# destination = "C:\\Users\\utkarsh\\Desktop\moved_file.txt"
destination = "C:\\Users\\utkarsh\\Desktop\\folder1"

try:
    if(os.path.exists(destination)):
        print("There is already a file there") 
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " Was not found.")    