# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler

class Euler(BaseEuler):
    def solve(self):
        lst = list(range(1, 101))
        res = (sum(lst)**2) - (sum(map(lambda x: x**2, lst)))
        print("The difference between the sum of the squares\n" +
              "and the square of the sum of the first 100 numbers\n" +
              "is: %d" % res)

    @property
    def problem(self):
        return '''
Project Euler Problem 6:

   The sum of the squares of the first ten natural numbers is,

   1**2 + 2**2 + ... + 10**2 = 385

   The square of the sum of the first ten natural numbers is,

   (1 + 2 + ... + 10)**2 = 55**2 = 3025

   Hence the difference between the sum of the squares of the
   first ten natural numbers and the square of the sum is
   3025  385 = 2640.

   Find the difference between the sum of the squares of the
   first one hundred natural numbers and the square of the sum.

'''
