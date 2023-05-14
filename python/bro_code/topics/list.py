food = ["pizza", "maggie"] 
print(food[0]) 

# list are mutable 
food[0] = "roti" 
print(food[0]) 

for x in food:
    print(x)

food.append("ice cream") 
food.remove("pizza")  
food.pop()
food.insert(0, "cake")
food.sort() 
food.clear() # clears everything from the list 

