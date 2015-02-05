# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.util import factorial


class Euler(BaseEuler):
    def solve(self):
        return sum([int(x) for x in str(factorial(100))])

    @property
    def answer(self):
        return ('The sum of the digits in the number 100! is: %d'
                % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 20:

    n! means n * (n - 1) * ... * 3 * 2 * 1

    For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800, and the
    sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
'''
