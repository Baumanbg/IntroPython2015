
from sum_double import sum_double

def test_3_5():
    assert sum_double(3,5) == 8
    
def test_5_5():
    assert sum_double(5,5) == 20
    
def test_neg5_5():
    assert sum_double(-5,5) == 0
    
def test_neg5_neg5():
    assert sum_double(-5,-5) == -20
    