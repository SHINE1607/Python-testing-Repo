import pytest
from src.shapes import Square

# for class based test, we could add setup_tool function to setup objects
# but funnction based tests, we could  add fictures



def test_area():
    square = Square(2)
    assert square.area() == 4
    
def test_perimeter(my_square):
    assert my_square.perimeter() == 8
    

def test_not_equal(my_square, weird_square):
    assert my_square != weird_square
    
    