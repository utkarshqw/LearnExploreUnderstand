class Car:
    # the following is class varialbe
    wheels = 4 # by default every vehicle would have 4 values 

    def __init__(self, make, model, year, color): # while calling the function we do not need the self in the argument 
        self.make = make      # these are instance variables and each one of them can have unique values 
        self.model = model   # these are instance variables and each one of them can have unique values 
        self.year = year    # these are instance variables and each one of them can have unique values 
        self.color = color   # these are instance variables and each one of them can have unique values 
    # def drive(self):
    #     print("This " + self.model + " is driving")
    
    # def stop(self):
    #     print("This " + self.model +  "  is stopped")

    




