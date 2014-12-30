# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def solve(self):
        res = [x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]
        return sum(res)

    @property
    def answer(self):
        return ('The sum of all the multiples of 3 or 5 below 1000 is: %d'
                % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 1:

   If we list all the natural numbers below 10 that are
   multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
   these multiples is 23.

   Find the sum of all the multiples of 3 or 5 below 1000.
'''
