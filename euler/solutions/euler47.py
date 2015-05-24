# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from math import ceil, sqrt


class Euler(BaseEuler):
    def solve(self):
        i = 1
        n = 210         # first number with 4 unique prime factors - start here
        while i != 4:
            n += 1
            if len(set(self._factor(n))) == 4: #if it has 4 unique prime factors
                i += 1
            else:
                i = 0
        return n - 3    # return the first of 4 consecutive

    def _factor(self, n):
        if n <= 1:
            return []
        p = next((x for x in range(2, ceil(sqrt(n)) + 1) if n % x == 0), n)
        return [p] + self._factor(n // p)

    @property
    def answer(self):
        return ('The first of 4 consecutive numbers to have 4 unique ' +
                'prime factors is %d.' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 47

    The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors
    are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime
    factors. What is the first of these numbers?
'''
