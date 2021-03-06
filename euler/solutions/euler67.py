# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.solutions.euler18 import get_triangle, find_max_sum
from os import path, getcwd


class Euler(BaseEuler):
    def solve(self):
        fp = path.join(getcwd(), 'euler/resources/triangle.txt')
        with open(fp, 'r') as f:
            return find_max_sum(get_triangle(f.read()))

    @property
    def answer(self):
        return ('The maximum sum travelling from the top of the triangle ' +
                'to the base is: %d' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 67:

    By starting at the top of the triangle below and moving to adjacent numbers
    on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in triangle.txt (right click and
    'Save Link/Target As...'), a 15K text file containing a triangle with
    one-hundred rows.

    NOTE: This is a much more difficult version of Problem 18. It is not
    possible to try every route to solve this problem, as there are 2^99
    altogether! If you could check one trillion (10^12) routes every second it
    would take over twenty billion years to check them all. There is an
    efficient algorithm to solve it. ;o)
'''
