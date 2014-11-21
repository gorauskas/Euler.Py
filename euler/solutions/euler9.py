# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from functools import reduce


class Euler(BaseEuler):
    def solve(self):
        t = []
        for i in range(1, 500):
            for j in range(i + 1, 500):
                a = int(j * j - i * i)
                b = 2 * j * i
                c = int(j * j + i * i)

                if a + b + c == 1000:
                    t = [a, b, c]
                    break

        print('The pythagorean triple whose sum equals 1000 is: ' +
              '%s\nThe product of this triple is: %d'
              % (sorted(t), reduce(lambda x, y: x * y, t)))

    @property
    def problem(self):
        return '''
Project Euler Problem 9:

   A Pythagorean triplet is a set of three natural numbers, a < b < c,
   for which,

    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

   There exists exactly one Pythagorean triplet for which a + b + c = 1000.
   Find the product abc.
'''
