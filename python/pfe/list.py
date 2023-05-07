# array is known as list in python 
# list are mutable but string are not 

list = [1, 2, 3, 4, 5, 6, 7]
# range() method 
print(range(len(list)))

for i in range(len(list)) :
    num = list[i]
    print("The number at posotion",i+1,"is", num)

# lists B 
 
a = [1, 2, 3] 
b = [4, 5, 6] 
c = a + b  # same if I have do in js i would need spread operator
print(c) # res would be [1, 2, 3, 4, 5, 6] 

# slicing list 
t = [9, 24, 12, 3, 74, 15] 
print(t[1:3]) 

# list methods 

stuff = []
stuff.append("book")
stuff.append(99)
print(stuff)
 
 # js includes function 
some = [1, 9, 21, 10, 16] 
print(9 in some) # true
print(15 in some) # false 
print(20 not in some) # true 

# sort() method 
friends = ["Joseph", "Glenn", "Sally"] 
friends.sort()
print(friends)

# len ()
# max () 
# min ()
# sum () 

# text = "abc"
# arr = list(text) 
# print(arr)

# append method is used to push a item at the end of list 


#list c 

#split method 
abc = "With three words"
stuff = abc.split() 
print("split method",stuff) 

abc = "with/three/words"
stuff = abc.split("/") 
print("split at /", stuff)


