#  super() = Function used to give access to the methods of a parent class. 
            #  Returns a temporary object of a prent class when used 

class Rectangle:
    def __init__ (self, length, width):
        self.length = length 
        self.width = width 


class Square(Rectangle):

    def __init__ (self, length, width):
        super().__init__(length, width)
    def area(self):
        return self.length * self.width
        

class Cube(Rectangle):

    def __init__ (self, length, width, height):
        super().__init__(length, width)
        self.height = height 
    
    def volume(self):
        return self.length * self.width * self.height


square = Square(3, 3)
cube = Cube(3, 3, 3) 

print(square.area()) 
print(cube.volume()) 



# class Square(Rectangle):

#     def _init_ (self, length, width):
#         self.length = length 
#         self.width = width 

# class Cube(Rectangle):

#     def _init_ (self, length, width, height):
#         self.length = length   
#         self.width = width 
#         self.height = height 
# we are repeating self.width and self.length above 

# updating the above code 