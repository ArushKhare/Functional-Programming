from typing import *
from typeguard import typechecked

# Currying allows us to delay passing in all the function inputs. This gives us 
# more flexibility in defining functions.

# Similar in style to SML (Standard ML)
# These functions are curried

@typechecked
def map(f: Callable):
    def fun(A: List):
        if (A == []):
            return []
        return [f(A[0])] + map(f)(A[1::])
    return fun

@typechecked
def filter(f: Callable):
    def fun(A: List):
        if (A == []):
            return []
        return [A[0]] + filter(f)(A[1::]) if f(A[0]) else filter(f)(A[1::])
    return fun

@typechecked
def compose(f: Callable):
    def fun(g: Callable):
        return lambda x: f(g(x))
    return fun

@typechecked
def foldl(f: Callable):
    def fun1(z):
        def fun2(L: List):
            if (L == []):
                return z
            return foldl(f)(f(L[0], z))(L[1::])
        return fun2
    return fun1
    
@typechecked
def foldr(f: Callable):
    def fun1(z):
        def fun2(L: List):
            if (L == []):
                return z
            return f(L[0], foldr(f)(z)(L[1::]))
        return fun2
    return fun1

@typechecked
def scan(f: Callable):
    def fun1(z):
        def fun2(L: List):
            if (L == []):
                return []
            return [f(L[0], z)] + scan(f)(f(L[0], z))(L[1::])
        return fun2
    return fun1

if __name__ == '__main__':
    # List Reverse
        print("Reverse Test 1:", foldl(lambda x, A : [x] + A) ([]) ([1, 2, 3, 4])) # Results in [4, 3, 2, 1]
        print("Reverse Test 2:", foldr(lambda x, A : A + [x]) ([]) ([1, 2, 3, 4])) # Results in [4, 3, 2, 1]
    # List Sum
        print("List Sum Test 1:", foldl(lambda x, y : x + y) (0) ([1, 2, 3, 4])) # Results in 10
        print("List Sum Test 2:", foldr(lambda x, y : x + y) (0) ([1, 2, 3, 4])) # Results in 10
    # Factorial
        print("Factorial Test 1:", foldl(lambda x, y : x * y) (1) ([1, 2, 3, 4])) # Results in 24
        print("Factorial Test 2:", foldr(lambda x, y : x * y) (1) ([1, 2, 3, 4])) # Results in 24
    # Factorial Sequence
        print("Factorial Sequence Test 1:", scan(lambda x, y : x * y) (1) ([1, 2, 3, 4])) # Results in [1, 2, 6, 24]
    # Prefix Sum
        print("Prefix Sum Test 1:", scan(lambda x, y : x + y) (0) ([1, 2, 3, 4])) # Results in [1, 3, 6, 10]
    # Remove all values
        print("Filter Test 1:", filter(lambda x : x != 4) ([1, 4, 3, 2, 5, 4, -1, 10])) # Results in [1, 3, 2, 5, -1, 10]
    # Shrink all values
        A = [10, 11, -10, -2, 6]
        print("Shrink Test 1:", map(lambda x : x - A[0]) (A)) # Results in [0, 1, -20, -12, -4]
