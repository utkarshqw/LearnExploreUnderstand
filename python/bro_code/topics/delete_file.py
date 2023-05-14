import os 
import shutil 

# path = "delete.txt"
path = "delete_folder"

path = "folder" # testing for non-empty folder

try:
    # os.remove(path) # this function does not remove empty folders 
    # os.rmdir(path) # used to rm dir
    shutil.rmtree(path) # to del non-empty dir
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete a non-empty folder with rmdir method")    
else:
    print(path + " was deleted") 













