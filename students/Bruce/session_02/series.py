def fibonacci(n):
    """Calculate the next number in a Fibonacci series where the previous two numbers are summed"""
    if n<= 3: return 1
    else: return fibonacci(n-2)+fibonacci(n-1)
n=int(input("Enter integer greater than 1: \n"))
fibnumber = fibonacci(n)
print("The Fibonacci number at position ",n,"is ",fibnumber)
def lucas(n):
    """Calculate the next number in a Lucas series where the previous two numbers are summed"""
    if n==1: return 2
    if n==2: return 1
    if n==3: return 3
    if n==4: return 4
    else: return lucas(n-2)+lucas(n-1)
lucasnumber = lucas(n)
print("The Lucas number at position ",n,"is ",lucasnumber)
"""This is how far I got - yes, I know it uses some brute force"""