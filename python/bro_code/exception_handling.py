# exception interrupt the flow of program 

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator 
#     print(result)
# except Exception: # this is not considered a good practice to have only a singe except block have multiple 
#      print("something went wrong :(")
    
# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator 
#     print(result)
# except ZeroDivisionError:
#     print("You can't divinde by zero!!!")  
# except ValueError:
#     print("Enter only numbers please")      


try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator 
   
except ZeroDivisionError as e:
    print(e)
    print("You can't divinde by zero!!!")  
except ValueError as e:
    print(e)
    print("Enter only numbers please")  
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result) # if there is no exception then only we print the result
finally:
    print("This will always execute")
