# dict a
purse  = dict() 
purse["money"] = 1 
purse["candy"] = 3 
purse["tissues"] = 75 
print(purse)

# list
lst = list() 
lst.append(21) 
print(lst[0]) 

# dictionary literals 
jjj = {"chuck":1, "fred": 42, "jan": 100} 
print(jjj) 

# dictionaries B 
# counting the frequency of things 

names = ["a", "a", "a","b", "b", "b", "c", "c"] 
counts = dict() 
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)        

# get method of dictionaries 
# for getting a default value of valiable if it does not exixts in the dictionary 

# if name in counts: 
#     x = counts[name]
# else:
#     x = 0
# or we can use the following code
# x = counts.get(name, 0) 

# get() method implementation 
counts = dict() 
names = ["csev", "cwen", "xqian", "cwen"] 
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

# Dictionaries C 

# looping through objects/dictionaries 

counts = {"chuck": 4, "fred": 42, "jan": 100} 
for key in counts: 
    print(key, counts[key])

jjj = {"chuck": 1, "fred": 42, "jan": 100} 
print(list(jjj)) 
print(jjj.keys()) 
print(jjj.values()) 
print(jjj.items()) 

# double variable for key in object loop 

for aaa, bbb in counts.items(): 
    print(aaa, bbb) 


#dict c 7:32

handle = open("sample.txt") 

counts = dict() 
for line in handle :
    words = line.split() 
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts) 

bigcount = None 
bigword = None 
for word, count in counts.items():
    if bigcount is None  or count > bigcount:
        bigword = word 
        bigcount = count 

print(bigword, bigcount)