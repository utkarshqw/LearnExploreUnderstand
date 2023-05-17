class Car:
   
    def __init__(self, make, model, year, color): # while calling the function we do not need the self in the argument 
        self.make = make
        self.model = model
        self.year = year 
        self.color = color
    def drive(self):
        print("This " + self.model + " is driving")
    
    def stop(self):
        print("This " + self.model +  "  is stopped")




