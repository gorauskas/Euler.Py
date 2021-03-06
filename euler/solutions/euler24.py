# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from itertools import permutations as p


class Euler(BaseEuler):
    def solve(self):
        return int(''.join([str(x) for x in sorted(p(range(10)))[999999]]))

    @property
    def answer(self):
        return ('The millionth lexicographic permutation of the digits 0 ' +
                'to 9 is: %d' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 24:

    A permutation is an ordered arrangement of objects. For example, 3124 is
    one possible permutation of the digits 1, 2, 3 and 4. If all of the
    permutations are listed numerically or alphabetically, we call it
    lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
    4, 5, 6, 7, 8 and 9?
'''
