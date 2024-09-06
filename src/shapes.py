from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Square(Shape):
    
    def __init__(self, side):
        self.side = side

    def __eq__(self, other) -> bool:
        if not isinstance(other, Square):
            return False
        
        return other.side == self.side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    
    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return 2 * (self.side1 + self.side2)
