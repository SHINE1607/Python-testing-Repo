import pytest
from src.shapes import Rectangle

@pytest.mark.parametrize("side1, side2, expected_area", [(1, 1, 1), (3, 9, 27), (11, 3, 33), (5, 3, 15)])
def test_multiple_rectangle_areas(side1, side2, expected_area):
    assert Rectangle(side1, side2).area() == expected_area