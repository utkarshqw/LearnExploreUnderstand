import random 
 
x = random.randint(1,6) # inclusive 1 and 6
print(x) 

# random floating point number
y = random.random() 
print(y)

myList = ["rock", "paper", "scissors"] 
z = random.choice(myList)
print(z) 

print(z) 

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"] 
random.shuffle(cards)  
print(cards) 