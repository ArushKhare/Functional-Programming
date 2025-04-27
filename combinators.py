from typing import *
from typeguard import typechecked

# Combinators are great and versatile because they allow us to easily combine 
# operations of two functions. They can be applied to any two functions (as long
# as the types of the functions are legal).

@typechecked
def add(f: Callable):
    def fun(g: Callable):
        return lambda x : f(x)+g(x)
    return fun
    
@typechecked
def sub(f: Callable):
    def fun(g: Callable):
        return lambda x : f(x)-g(x)
    return fun
    
@typechecked
def mult(f: Callable):
    def fun(g: Callable):
        return lambda x : f(x)*g(x)
    return fun
    
@typechecked
def compose(f: Callable):
    def fun(g: Callable):
        return lambda x : f(g(x))
    return fun

@typechecked   
def div(f: Callable):
    def fun(g: Callable):
        return lambda x : f(x)/g(x)
    return fun
    
@typechecked
def intdiv(f: Callable):
    def fun(g: Callable):
        return lambda x : f(x)//g(x)
    return fun
    
@typechecked
def mod(f: Callable):
    def fun(g: Callable):
        return lambda x : f(x)%g(x)
    return fun

if __name__ == '__main__':
    # Test add
    a = add(lambda x : x + 1)(lambda x : x - 1)
    print("b(2) =", a(2)) # Should result in 4

    # Test sub
    b = sub(lambda x : x + 1)(lambda x : x - 1)
    print("b(2) =", b(2)) # Should result in 2

    # Test mult
    c = mult(lambda x : x + 1)(lambda x : x - 1)
    print("c(2) =", c(2)) # Should result in 3

    # Test compose
    d = compose(lambda x : x + 1)(lambda x : x - 1)
    print("d(2) =", d(2)) # Should result in 2 (no change since both functions are inverses of each other)

    # Test div
    f = div(lambda x : x + 1)(lambda x : x - 1)
    print("f(2) =", f(2)) # Should result in 3.0

    # Test intdiv
    g = intdiv(lambda x : x + 1)(lambda x : x - 1)
    print("g(2) =", g(2)) # Should result in 3

    # Test mod
    h = mod(lambda x : x + 1)(lambda x : x - 1)
    print("h(2) =", h(2)) # Should result in 0