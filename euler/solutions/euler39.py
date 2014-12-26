# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def solve(self):
        result = 0
        resultSolutions = 0

        p = 2
        while p <= 1000:
            numberOfSolutions = 0

            a = 2
            while a < (p / 3):
                if p * (p - 2 * a) % (2 * (p - a)) == 0:
                    numberOfSolutions += 1
                a += 1

            if numberOfSolutions > resultSolutions:
                resultSolutions = numberOfSolutions
                result = p

            p += 2

        print('The number of solutions is maximized for %d' % int(result))

    @property
    def problem(self):
        return '''
Project Euler Problem 39:

    If p is the perimeter of a right angle triangle with integral length sides,
    {a,b,c}, there are exactly three solutions for p = 120.

        {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?
'''
