from typing import *
from typeguard import typechecked
from HOF import *

# This code uses a form of lazy evaluation to derive a sequence of values based on
# a function. This is very efficient because lazy evaluation means that we only
# calculate when we want them.

class InfiniteSeq:

    @typechecked
    def __init__(self, f: Callable, seed = 0):
        self.S = []
        self.fun = f
        self.lazy = lambda : (lambda : seed, lambda : self.fun(seed))

    def next(self):
        r = (self.lazy)()
        self.S.append(r[1])
        self.lazy = lambda : (lambda : r[0]() + 1, lambda : self.fun((r[0]()) + 1))

    def __str__(self):
        return str(maps(lambda f : f())(self.S))


I = InfiniteSeq(lambda x : x**2)
print(I)
I.next()
print(I)
I.next()
print(I)
I.next()
print(I)
I.next()
print(I)
I.next()
print(I)