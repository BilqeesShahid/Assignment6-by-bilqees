#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-9-Abstract Classes and Methods
#Use the abc module to create an abstract class Shape with an abstract method area(). 
#Inherit a class Rectangle that implements area().
 
 
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete class inheriting and implementing abstract method

#Area of Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create object and call the method
rect = Rectangle(5, 10)
print("Area of rectangle:", rect.area()) #output: 50

#Area of Square

class Square(Shape):
    def __init__(self, side):
        self.side = side
         

    def area(self):
        return self.side * self.side

# Create object and call the method
squa = Square(10)
print("Area of rectangle:", squa.area()) #output:100
