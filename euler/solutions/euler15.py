# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.util import factorial


'''
research

This is a combinations problem. on a 20x20 grid to get from top-left to
bottom-right there are 40 moves (20 down and 20 right). The problem can be
solved by applying the formula for the central binomial coefficient
(http://en.wikipedia.org/wiki/Central_binomial_coefficient):

             x!
C(x,y) = -----------
         y! * (x-y)!

'''


class Euler(BaseEuler):
    def solve(self):
        routes = lambda x, y: factorial(x) / (factorial(x - y) * factorial(y))
        print('There are %d routes through a 20x20 grid' % routes(40, 20))

    @property
    def problem(self):
        return '''
Project Euler Problem 15:

    Starting in the top left corner of a 2x2 grid, there are 6 routes
    (without backtracking) to the bottom right corner.

    How many routes are there through a 20x20 grid?
'''
