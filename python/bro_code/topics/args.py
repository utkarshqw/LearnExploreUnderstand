# *args(* is only necessary args can be replaced by any str)
# useful so that a function can accept a varying amount of arguments
# suppose we don't know the number of arguments 
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum     
print(add(1,2,3, 4, 5, 6))    

# *args are tuples(imutable) 
# can be converted to list 
def add2(*args):
    sum = 0
    stuff = list(args) 
    stuff[0] = 0
    for i in stuff:
        sum += i 
    return sum 
print(add2(1, 2, 3, 4, 5, 6))


