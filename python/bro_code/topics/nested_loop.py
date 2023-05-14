# rows = int(input("How many rows?: ")) 
# columns = int(input("How many columns?: ")) 
# symbol = input("Enter a symbol to use: ") 

rows = 3
columns = 4
symbol = "@"    
for i in range(rows):
    for j in range(columns): 
        print(symbol, end="") # @ is not printed on new line 
    print() # this is giving us a new line 

