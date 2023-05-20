class Animal:
 
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    # if overriding make the same function with same args..
    def eat(self):  # using the same eat function but overring it with info specific to rabbit 
        print("This rabbit is eating a carrot") 


rabbit = Rabbit() 
# basically the Rabbit will first see for eat function within it self then it's parent 
rabbit.eat() 

