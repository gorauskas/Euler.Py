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


class FibonacciDigitLengthSequence:
    def __init__(self):
        pass

    def _digit_len(self, n):
        return len(str(n))

    def __iter__(self):
        self.a, self.b = 0, 1
        self.idx = 0
        return self

    def __next__(self):
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        t = (self.idx, self._digit_len(fib))
        self.idx += 1
        return t


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
    '''
    This prime number generator will churn out primes from the first prime
    above 0 (2) until you tell it to stop.
    '''
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


def PrimeRange(start, end=None):
    '''
    This prime number generator will churn out primes whose number value are
    higher than `start` and lower than `end`.

    e.g.: `print(list(PrimeRange(10, 100)))` return the following:

    [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
     83, 89, 97]
    '''
    if not end:
        end = start
        start = 2
    m = set()
    for i in range(2, end):
        if i not in m:
            if i >= start:
                yield i
            if i * i < end:
                m.update(range(i * i, end, i))
