# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def solve(self):
        ls = 0

        for i in range(1, 100):
            for j in range(1, 100):
                n = i ** j
                s = sum([int(d) for d in list(str(n))])
                if s > ls:
                    ls = s

        return ls

    @property
    def answer(self):
        return ('The max digital sum is %d.' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 56

    A googol (10^100) is a massive number: one followed by one-hundred zeros;
    100^100 is almost unimaginably large: one followed by two-hundred
    zeros. Despite their size, the sum of the digits in each number is only 1.

    Considering natural numbers of the form, a^b, where a, b < 100, what is the
    maximum digital sum?
'''
