import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='') 
mysock.close() 

# Networking: Text rocessing 
# 7-5-2023 

print(ord( "H")) # know ASCII REPRESENTATION 

#UNICODE 
# is re commended practice for encoding data to be exchanged between systems  
# UTF-8 has dynamic length 

# using urllib in python 

# import urllib.request
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

# web scraping with python 
# we can retriev a webpage with python and we can scrape data from tat 


