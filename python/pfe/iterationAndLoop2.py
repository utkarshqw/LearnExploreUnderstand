# while loop and break statement 
n = 0
while True:
    if n==3:
        break
    print(n)
    n = n+1

# for in loop, Definite loops 

arr = [1, 2, 3, 4, 5] 
for key in arr:
    print(key)


# largest number in a array 
arr = [9, 41, 12, 3, 74, 15]
largest = -1
for key in arr:
    if  key > largest:
        largest = key 
print("The largest number is",largest)

# print with serial number 

start = 0
for key in arr:
    start = start + 1
    print(start, key)
print("The current value of start",start)

# find sum of all the items in array 

sum = 0
for key in arr:
    sum += key
print("The sum is",sum)

# fine average in a loop 

sum = 0
count = 0
print("length of arr is",len(arr))

for key in arr:
    sum += key 
    count += 1
print("The average is",sum/count)

# find number greater than 20 filtering 

for key in arr:
    if key > 20:
        print("Large number", key)
    if key == 3:
        print("the specific number is found",key == 3, key)   


# "is" or == and "is not" or != 
n = 1
print(n is 1)
print(n is not 1)

# which is false 
print(0 == 0.0)
print(0 is 0.0)
print(0 is not 0.0)

# the is operaator check the address but the == operator checks the value 








