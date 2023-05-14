import os 
# have to add one more \ after \ becuase it is the escape sequence for it withing a string 
# path =  "C:\\Users\\utkarsh\\Desktop\\text.txt" 
path =  "C:\\Users\\utkarsh\\Desktop\\text" 

if os.path.exists(path):
    print("That location exists") 
    # check if the location has file or not
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("The is a directory")
else:
    print("That location doesn't exist!") 
