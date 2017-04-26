# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def solve(self):
        def f(x): return sorted(str(x))

        n = 99999
        while not f(n * 2) == f(n * 3) == f(n * 4) == f(n * 5) == f(n * 6):
            n += 9

        return n

    @property
    def answer(self):
        return ('The smallest positive integer is %d.' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 52

    It can be seen that the number, 125874, and its double, 251748, contain
    exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits.
'''
