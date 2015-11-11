
""" Given two int values, return their sum; unless the two values are
 the same, then return double their sum.  The code indicates three
 different approaches."""

def sum_double(a,b):
    #if a == b:
    #    return 2*(a+b)
    #else:
    #    return a + b
    
    """ or """
    
    #if a == b: return 2*(a+b)
    #else: return a + b
    
    """ or """
    
    y = 2*(a+b) if a == b else a + b  #ternary expression
    return y
    
sum_double(2,2)