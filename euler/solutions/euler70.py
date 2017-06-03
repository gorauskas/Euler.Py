# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.sequences import PrimeRange
from itertools import combinations as combos


class Euler(BaseEuler):
    def solve(self):
        limit = 10 ** 7
        minn, res = float('Inf'), None
        primes = list(PrimeRange(1, 2 * int(limit ** 0.5)))

        for p1, p2 in combos(primes, 2):
            if p1 * p2 < limit:
                n, d = p1 * p2, (p1 - 1) * (p2 - 1)
                if sorted(str(n)) == sorted(str(d)):
                    if n / d < minn:
                        minn = n / d
                        res = n

        return res

    @property
    def answer(self):
        return ('The minimum value of n is %d' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 70:

    Euler's Totient function, φ(n) [sometimes called the phi function], is used
    to determine the number of positive numbers less than or equal to n which
    are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
    less than nine and relatively prime to nine, φ(9)=6.

    The number 1 is considered to be relatively prime to every positive number,
    so φ(1)=1.

    Interestingly, φ(87109)=79180, and it can be seen that 87109 is a
    permutation of 79180.

    Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and
    the ratio n/φ(n) produces a minimum.
'''
