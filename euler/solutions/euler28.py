# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


'''
You don't have to actually construct the spiral to solve this problem.
this is a simple summation problem and therefore the result can be expressed
by a formula which is presented below
'''


class Euler(BaseEuler):
    def solve(self):
        n = 500  # we focus on the rings => a 1001x1001 spiral has 500 rings
        return ((16 * (n ** 3) + 26 * n) / 3 + 10 * (n ** 2)) + 1

    @property
    def answer(self):
        return ('The sum of the numbers on the diagonals in a 1001 by 1001 ' +
                'spiral is %d' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 28:

    Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
    formed in the same way?
'''
