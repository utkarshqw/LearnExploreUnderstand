# multiple inheritance = when a child class is derived from more than one parent class 

class Prey:
    def flee(self):
        print( self.name +  " animal flees")

class Predator:
    def hunt(self):
        print( self.name+" animal is hunting") 

# some animal can flee 
# some animal can hunt 
# some can do both(fish)

class Rabbit(Prey):
    name = "rabbit"
    pass

class Hawk(Predator):
    name = "hawk"
    pass

class Fish(Prey, Predator):
    name = "fish"
    pass 

rabbit = Rabbit()
hawk = Hawk()
fish = Fish() 

rabbit.flee() 
hawk.hunt() 
fish.flee()
fish.hunt() 










