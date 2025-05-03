from typing import *
from typeguard import typechecked

# Similar in style to SML (Standard ML)
# These higher-order functions are curried

@typechecked
def maps(f: Callable) -> Callable:
    def fun(A: List) -> List:
        if (A == []):
            return []
        return [f(A[0])] + maps(f)(A[1::])
    return fun

@typechecked
def filters(f: Callable) -> Callable:
    def fun(A: List) -> List:
        if (A == []):
            return []
        return [A[0]] + filters(f)(A[1::]) if f(A[0]) else filters(f)(A[1::])
    return fun

@typechecked
def compose(f: Callable) -> Callable:
    def fun(g: Callable) -> Callable:
        return lambda x: f(g(x))
    return fun

@typechecked
def foldl(f: Callable) -> Callable:
    def fun1(z) -> Callable:
        def fun2(L: List):
            if (L == []):
                return z
            return foldl(f)(f(L[0], z))(L[1::])
        return fun2
    return fun1
    
@typechecked
def foldr(f: Callable) -> Callable:
    def fun1(z) -> Callable:
        def fun2(L: List):
            if (L == []):
                return z
            return f(L[0], foldr(f)(z)(L[1::]))
        return fun2
    return fun1

@typechecked
def scan(f: Callable) -> Callable:
    def fun1(z) -> Callable:
        def fun2(L: List) -> List:
            if (L == []):
                return []
            return [f(L[0], z)] + scan(f)(f(L[0], z))(L[1::])
        return fun2
    return fun1
