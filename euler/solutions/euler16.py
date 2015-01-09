# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def solve(self):
        return sum([int(x) for x in str(2 ** 1000)])

    @property
    def answer(self):
        return ('The sum of the digits of the number 2^1000 is: %d'
                % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 16:

    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
'''
