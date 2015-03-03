# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.util import is_pandigital


class Euler(BaseEuler):
    def solve(self):
        p = set()
        for i in range(1, 101):
            start = 1234
            if i > 9:
                start = 123
            for j in range(start, int(10000 / i) + 1):
                s = '%d%d%d' % (i, j, i * j)
                if is_pandigital(int(s)):
                    p.add(i * j)

        return sum(p)

    @property
    def answer(self):
        return ('The sum of all products whose ' +
                'multiplicand/multiplier/product\nidentity can be written ' +
                'as a 1 through 9 pandigital is %d' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 32:

    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234,
    is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
    multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product
    identity can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to
    only include it once in your sum.
'''
