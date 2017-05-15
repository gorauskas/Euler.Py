# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.sequences import PrimeRange
from euler.util import is_prime
import itertools


class Euler(BaseEuler):
    def __init__(self):
        # self._primes = gen_primes(10000)
        self._primes = list(PrimeRange(1, 10000))
        self._ss = 5

    def solve(self):
        c = 0
        while not c:
            c = self._chain([self._primes.pop(0)])

        return sum(map(int, c))

    def _chain(self, c):
        if len(c) == self._ss:
            return c
        for p in self._primes:
            if p > c[-1] and self._c_primes(c + [p]):
                nc = self._chain(c + [p])
                if nc:
                    return nc
        return False

    def _c_primes(self, c):
        return all(is_prime(str(p[0]) + str(p[1]))
                   for p in itertools.permutations(c, 2))

    @property
    def answer(self):
        return ('The lowest sum for a set of five primes is ' +
                '%d.' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 60

    The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
    primes and concatenating them in any order the result will always be
    prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum
    of these four primes, 792, represents the lowest sum for a set of four
    primes with this property.

    Find the lowest sum for a set of five primes for which any two primes
    concatenate to produce another prime.
'''
