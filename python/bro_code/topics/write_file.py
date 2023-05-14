text = "Yooooo\nThis text is inserted witht the help of python"
with open("write_file.txt", "w") as file:
    file.write(text)

# we can also append text and not overwrite the existing text file 
text = "\nThis text is appended"
with open("write_file.txt", "a") as file:
    file.write(text)