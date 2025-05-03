from infix import *
from typing import *
from typeguard import typechecked

@or_infix
@typechecked
def add(f: Callable, g: Callable): # f(x) + g(x)
    return lambda x : f(x)+g(x)

@or_infix  
@typechecked
def sub(f: Callable, g: Callable): # f(x) - g(x)
    return lambda x : f(x)-g(x)

@or_infix   
@typechecked
def mul(f: Callable, g: Callable): # f(x) * g(x)
    return lambda x : f(x)*g(x)

@or_infix    
@typechecked
def of(f: Callable, g: Callable): # f(g(x))
    return lambda x : f(g(x))
