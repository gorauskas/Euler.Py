# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from math import log10


class Euler(BaseEuler):
    def solve(self):
        L, n, d, c = 1000, 3, 2, 0

        for x in range(2, L + 1):
            n, d = n + 2 * d, n + d
            if int(log10(n)) > int(log10(d)):
                c += 1

        return c

    @property
    def answer(self):
        return ('There are %d fractions whose numerators ' % self.solve() +
                'have more digits\nthan then denominator.')

    @property
    def problem(self):
        return '''
Project Euler Problem 57

    It is possible to show that the square root of two can be expressed as an
    infinite continued fraction.

      √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

    By expanding this for the first four iterations, we get:

      1 + 1/2 = 3/2 = 1.5
      1 + 1/(2 + 1/2) = 7/5 = 1.4
      1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
      1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

    The next three expansions are 99/70, 239/169, and 577/408, but the eighth
    expansion, 1393/985, is the first example where the number of digits in the
    numerator exceeds the number of digits in the denominator.

    In the first one-thousand expansions, how many fractions contain a
    numerator with more digits than denominator?
'''
