from abc import ABC, abstractmethod, abstractproperty

class Shape(ABC):
    @abstractproperty
    def area(self):
       pass
    
    @area.setter
    def area(self, value):
       pass
        
    @abstractproperty
    def perimeter(self):
       pass
   
    @perimeter.setter
    def area(self, value):
       pass
        
  
    def print_shape(self):
       pass

class Rectangle(Shape):
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter
     
    @property   
    def area(self):
        return self.__area
    
    @area.setter
    def area(self, value):
        if value > 0:
            self.__area = value
        else:
            raise ValueError("The area can not be negative!")
        
    @property
    def perimeter(self):
        return self.__perimeter
    
    @perimeter.setter
    def perimeter(self, value):
        if value > 0:
            self.__perimeter = value
        else:
            raise ValueError("The perimeter can not be negative!")
               
    def print_shape(self):
        print(f"Rectangle has area: {self.area} and perimeter: {self.perimeter}")
        
        
rectangle1 = Rectangle(10, 40)
rectangle1.area = 9
rectangle1.print_shape()
