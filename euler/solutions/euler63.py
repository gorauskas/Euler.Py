# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from math import log10


class Euler(BaseEuler):
    def solve(self):
        s = 0

        for n in range(1, 10):
            s += int(1 // (1 - log10(n)))

        return s

    @property
    def answer(self):
        return ('There are %d n-digit integers that ' % self.solve() +
                'are also an nth power.')

    @property
    def problem(self):
        return '''
Project Euler Problem 63

    The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit
    number, 134217728=89, is a ninth power.

    How many n-digit positive integers exist which are also an nth power?
'''
