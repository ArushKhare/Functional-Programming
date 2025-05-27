from typing import *
from typeguard import typechecked

# Continuation-passing style (CPS) allows us to add a continuation function as input. This 
# makes it easier for us to call continuation functions within our function.

# Similar in style to SML
# These functions are in CPS

@typechecked
def mapCPS(f: Callable):
    def fun(A: List):
        def con(k : Callable):
            if (A == []):
                return k([])
            return mapCPS(f)(A[1::])(lambda res : k([f(A[0])] + res))
        return con
    return fun

@typechecked
def filterCPS(f: Callable):
    def fun(A : List):
        def con(k: Callable):
            if (A == []):
                return k([])
            return filterCPS(f)(A[1::])(lambda res: k([A[0]] + res if f(A[0]) else res))
        return con
    return fun

@typechecked
def composeCPS(f: Callable):
    def fun(g: Callable):
        def con(k: Callable):
            return lambda x: k(f(g(x)))
        return con
    return fun

@typechecked
def foldlCPS(f: Callable):
    def fun1(z):
        def fun2(L: List):
            def con(k: Callable):
                if (L == []):
                    return k(z)
                return foldlCPS(f)(f(L[0], z))(L[1::])(k)
            return con
        return fun2
    return fun1

@typechecked
def foldrCPS(f: Callable):
    def fun1(z):
        def fun2(L: List):
            def con(k: Callable):
                if (L == []):
                    return k(z)
                return foldrCPS(f)(z)(L[1::])(lambda res: k(f(L[0], res)))
            return con
        return fun2
    return fun1

@typechecked
def scanCPS(f: Callable):
    def fun1(z):
        def fun2(L: List):
            def con(k : Callable):
                if (L == []):
                    return k([])
                return scanCPS(f)(f(L[0], z))(L[1::])(lambda res : k([f(L[0], z)] + res))
            return con
        return fun2
    return fun1

if __name__ == '__main__':
    # List Reverse
        print("Reverse Test 1:", foldlCPS(lambda x, A : [x] + A) ([]) ([1, 2, 3, 4])(lambda x : x)) # Results in [4, 3, 2, 1]
        print("Reverse Test 2:", foldrCPS(lambda x, A : A + [x]) ([]) ([1, 2, 3, 4])(lambda x : x)) # Results in [4, 3, 2, 1]
    # List Sum
        print("List Sum Test 1:", foldlCPS(lambda x, y : x + y) (0) ([1, 2, 3, 4])(lambda x : x)) # Results in 10
        print("List Sum Test 2:", foldrCPS(lambda x, y : x + y) (0) ([1, 2, 3, 4])(lambda x : x)) # Results in 10
    # Factorial
        print("Factorial Test 1:", foldlCPS(lambda x, y : x * y) (1) ([1, 2, 3, 4])(lambda x : x)) # Results in 24
        print("Factorial Test 2:", foldrCPS(lambda x, y : x * y) (1) ([1, 2, 3, 4])(lambda x : x)) # Results in 24
    # Factorial Sequence
        print("Factorial Sequence Test 1:", scanCPS(lambda x, y : x * y) (1) ([1, 2, 3, 4])(lambda x : x)) # Results in [1, 2, 6, 24]
    # Prefix Sum
        print("Prefix Sum Test 1:", scanCPS(lambda x, y : x + y) (0) ([1, 2, 3, 4])(lambda x : x)) # Results in [1, 3, 6, 10]
    # Remove all values
        print("Filter Test 1:", filterCPS(lambda x : x != 4) ([1, 4, 3, 2, 5, 4, -1, 10])(lambda x : x)) # Results in [1, 3, 2, 5, -1, 10]
    # Shrink all values
        A = [10, 11, -10, -2, 6]
        print("Shrink Test 1:", mapCPS(lambda x : x - A[0]) (A)(lambda x : x)) # Results in [0, 1, -20, -12, -4]
