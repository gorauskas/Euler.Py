# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from itertools import permutations as perms


"""
1. there are only 3,628,800 (10!) 0 to 9 pandigital numbers, so there's no need
   to examine all 10 billion 10-digit numbers.
2. consider only numbers whose last 3 digits divide by 17
3. now only check the permutations of the 7 remaining digits
4. this can be reduced further by considering the division by 13 and so on
"""


class Euler(BaseEuler):
    def __init__(self):
        self._F1 = lambda s: int(s[1:4]) % 2 == 0
        self._F2 = lambda s: int(s[2:5]) % 3 == 0
        self._F3 = lambda s: int(s[3:6]) % 5 == 0
        self._F4 = lambda s: int(s[4:7]) % 7 == 0
        self._F5 = lambda s: int(s[5:8]) % 11 == 0
        self._F6 = lambda s: int(s[6:9]) % 13 == 0
        self._F7 = lambda s: int(s[7:]) % 17 == 0

    def solve(self):
        t = list(perms('0123456789', 10))
        p = [''.join(s) for s in t]

        l = [i for i in p if self._F7(i)]
        l = [i for i in l if self._F6(i)]
        l = [i for i in l if self._F5(i)]
        l = [i for i in l if self._F4(i)]
        l = [i for i in l if self._F3(i)]
        l = [i for i in l if self._F2(i)]
        l = [i for i in l if self._F1(i)]

        return sum([int(i) for i in l])

    @property
    def answer(self):
        return ('The sum of all 0 to 9 pandigital numbers with this ' +
                'property is %d.' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

- d2d3d4=406 is divisible by 2
- d3d4d5=063 is divisible by 3
- d4d5d6=635 is divisible by 5
- d5d6d7=357 is divisible by 7
- d6d7d8=572 is divisible by 11
- d7d8d9=728 is divisible by 13
- d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''
