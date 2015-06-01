# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def solve(self):
        l = list(map(lambda x: x ** x, range(1, 1001)))
        s = sum(l)
        return int(str(s)[-10:])

    @property
    def answer(self):
        return ('The last 10 digits of the series is %d.' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 48

    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
'''
