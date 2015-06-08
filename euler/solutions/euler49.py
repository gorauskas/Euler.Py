# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.sequences import PrimeRange
from itertools import permutations as perms


class Euler(BaseEuler):
    def solve(self):
        pl = list(PrimeRange(1000, 10000))
        ps = set(pl)
        for p in pl:
            p = [p, p + 3330, p + 6660]
        if p[0] == 1487:
            continue
        if any(x not in ps for x in p[1:]):
            continue
        if any(tuple(str(x)) not in perms(str(p[0])) for x in p[1:]):
            continue
        return int(''.join([str(x) for x in p]))

    @property
    def answer(self):
        return ('The 12-digit number is %d.' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 49

    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways: (i) each of the three terms are
    prime, and, (ii) each of the 4-digit numbers are permutations of one
    another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit increasing
    sequence.

    What 12-digit number do you form by concatenating the three terms in this
    sequence?
'''
