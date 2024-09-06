import pytest
import src.my_functions as my_functions 


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5
    

def test_subtraction():
    result = my_functions.subtract(1, 4)
    assert result == -3

# Testing for a specific error condition
def test_divide():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(1, 0)
        
# makring slow test
@pytest.mark.slow
def test_slow():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(1, 0)
        
#skipping test
@pytest.mark.skip(reason="This feature is currently not supported")
def test_skip():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(1, 0)
        
@pytest.mark.xfail(reason='This is going to fail anyaway')
def test_divide():
    assert my_functions.divide(4, 1) == 4
    