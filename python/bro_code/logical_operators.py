temp = int(input("What is the temperature outside? "))

if temp >= 0 and temp <= 30:
    print("the temperature is good today!")
    print("go outside")
elif temp < 0 : 
    print("the temp is bad today")
    print("stay inside")
# not or we can say !(js) 
elif not(temp < 30):
    print("temp is more than 30")
    
