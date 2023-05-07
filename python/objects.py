class PartyAnimal: 
    x=0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x) 

an = PartyAnimal() 
an.party() 
an.party()
an.party()  

#  response 1, 2, 3 
y = "Hello world" 
x = dir(y) 
# print(x) 

# object lifecycle 

#  act of creating and destroying the objects 
# Constructor 
#  the code below is outdated I think. 
class PartyAnimal: 
    x = 0

    def _init_(self):
        print("I am consructed")

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)    
    def _del_(self):
        print("I am destructed", self.x)

    an = PartyAnimal() 
    an.party() 
    an.party() 
    an = 42 
    print("an contains", an) 

    #  but I have understood the concept of the above code I think the concept would not have changed much 

    # Inheritance or we can say extend
    
    class FootballFan(PartyAnimal):
        points = 0 
        def touchdown(self):
            self.points = self.points + 7
            self.party()
            print(self.name, "pints", self.points) 
    
    # if we wanted to extend a class to another class we simply have to put it inside of () what class is declared 
    
    
