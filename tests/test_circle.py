import pytest
import src.shapes as shapes


class TestCircle:
    
    def setup_method(self, method):
        print(f"Setting up method {method}")
        self.circle = shapes.Circle(10)  # this instance will be availabel in all the methods
    
    
    def test_area(self):
        assert self.circle.area() == (3.14 * self.circle.radius ** 2)
    
    def test_perimeter(self):
        assert self.circle.perimeter() == (2 * 3.14 * self.circle.radius)
    def test_one(self):
        assert True
        
    def test_two(self):
        assert True