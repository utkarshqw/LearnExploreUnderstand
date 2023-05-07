# Python Regular Expression Quick Guide

# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times 
#          (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times 
#          (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end

import re  # importing regualar express

#  using re module to read line including "Python"
hand = open("sample.txt")
for line in hand:
    line = line.rstrip()
    if re.search("Python", line):
        print(line)
# ^X.*: 
# ^ Match any character 
# X Match iteself 
# . Match any character 
# * Many times 

# ^X-\S+: 
# I want X- at the beginning of my string 
# Then I want a "\S" non white space character(+) one or more times 
# following string would match 
# X-Sieve: CMU Sieve 2.3 
# X-CDF-sdf: Innocent 


#RegEx B 
x = 'My 2 favorite numbers are 19 and 42' 
y = re.findall('[0-9]+',x) 
# find all gives the list of all the result 
# a square bracket is one character 
# so square will only search for one character 
# so we place + which makes our express to 
# find one digit or more number between 0-9 
print(y)

z = re.findall('[AEIOU]+', x)
print(z)

#Greedy matching 
x = "From: Using the : character" 
y = re.findall('^F.+:', x)  # greedy  choose larger if available 
z = re.findall('^F.+?:', x) # greedy  ? is to tell dont be greedy
# start with F one or more character last character should be : 
print(y)
print(z) 


# fine-tuning string extraction 
str = 'From stephaen.marquard@uct.ac.za Sat Jan 5 09:4:16 2008'
y = re.findall('^From (\S+@\S+)', str) 
print(y) 


y = re.findall('@([^ ]*)', str ) 
# [^ ] not a blank
print(y) 
y = re.findall('^From .*@([^ ]*)', str) 
print(y) 