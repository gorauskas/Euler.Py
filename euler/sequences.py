# -*- coding: utf-8 -*-

import itertools


class FibonacciSequence:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


class TriangleNumberSequence:
    def __init__(self):
        pass

    def __iter__(self):
        self.current = 0
        self.last = 0
        self.count = 0
        return self

    def __next__(self):
        self.last = self.current
        self.count += 1
        self.current = self.last + self.count
        return self.current


def PrimeGenerator():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = q
            yield q
        else:
            x = q + 2 * p
            while x in D:
                x += 2 * p
            D[x] = p
