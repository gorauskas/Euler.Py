# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.sequences import PrimeRange
from math import sqrt


class Euler(BaseEuler):
    def solve(self):
        return max((self._pell(n), n) for n in list(PrimeRange(1, 1000)))[1]

    def _pell(self, n):
        p, k, x, y, sd = 1, 1, 1, 0, sqrt(n)

        while k != 1 or y == 0:
            p = k * (p // k + 1) - p
            p = p - int((p - sd) // k) * k
            z = (p * x + n * y) // abs(k)
            y = (p * y + x) // abs(k)
            k = (p * p - n) // k
            x = z

        return z

    @property
    def answer(self):
        return ('The value of D is %d' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 66

    Consider quadratic Diophantine equations of the form:

        x2 – Dy2 = 1

    For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

    It can be assumed that there are no solutions in positive integers when D
    is square.

    By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
    following:

        32 – 2×22 = 1
        22 – 3×12 = 1
        92 – 5×42 = 1
        52 – 6×22 = 1
        82 – 7×32 = 1

    Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
    obtained when D=5.

    Find the value of D ≤ 1000 in minimal solutions of x for which the largest
    value of x is obtained.
'''
