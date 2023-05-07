x = ("Glenn", "Sally","Joseph")
print(x[2]) 

y = (1, 9, 2) 
print(y)

for key in y:
    print(key) 

#tuples are immutable 
#tuples are made for efficiency 
# x = (5, 4, 3) 
# x[2] = 0  // this will throw error 
 
# things not allowed in tuples 
#tuples.sort() 
# tuples.append(5)
# tuples.reverse()

#tuples method count(), index()
 
x, y = (4, 44)  
print(x, y) 

# the tuples collection 
# 6:43

d = dict() 
d["csev"] = 2 
d["cwen"] = 4 
print(d.items()) # list of tuples 
for (k, v)  in d.items(): 
    print(k, v)

# tuples are comparable 
# Once we get true tuples stops looking furtuer and returns true
a = (0, 1, 2) < (5, 1, 2) 
b = (0, 1, 200000) < (0, 3, 4) 
c = ("Jones", "Sally") < ("Jones", "Sam")
d = ("Jones", "Sally") < ("Adams", "sam")
print(a) 
print(b) 
print(c) 
print(d)  

# comparing and sorting tuples B 

# sorting lists of tuples 

d = {"a": 10, "b": 1, "c": 22}
print(d.items()) 
t = sorted(d.items())
for k, v in sorted(d.items()):
    print(k, v)
 

# sort by values instead of key 
c = {"a":10, "b":1, "c":22} 
temp = list() 
for k, v in c.items(): 
    temp.append((v,k)) 

print(temp) 
temp = sorted(temp, reverse=True)
print(temp)

# some shorter version of pyton code 

c = {"a":10, "b":1, "c":22} 
print(sorted([(v,k) for k, v in c.items()]))  



