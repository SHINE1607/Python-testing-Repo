import pytest
from src.shapes import Square


@pytest.fixture
def my_square():
    return Square(2)

@pytest.fixture
def weird_square():
    return Square(-2)