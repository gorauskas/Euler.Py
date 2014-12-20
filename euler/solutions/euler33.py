# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def solve(self):
        d = 1.0
        for i in range(1, 10):
            for j in range(1, i + 1):
                for k in range(1, j + 1):
                    ki = k * 10 + i
                    ij = float(i * 10 + j)
                    if k * ij == ki * j:
                        d *= ij / ki

        print('The value of the denominator is: %d' % d)

    @property
    def problem(self):
        return '''
Project Euler Problem 33:

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician
    in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
    which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less
    than one in value, and containing two digits in the numerator and
    denominator.

    If the product of these four fractions is given in its lowest common terms,
    find the value of the denominator.
'''
