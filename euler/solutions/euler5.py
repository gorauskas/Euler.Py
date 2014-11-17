# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from fractions import gcd
from functools import reduce

'''
Solve a simpler version of the problem. The lowest common multiple (LCM) of
two numbers x and y, usually denoted by lcm(x,y), is the smallest positive
number that is divisible by both x and y. You can do this by using the greatest
common divisor (GCD) function per the following formula:

               |x . y|
  lcm(x, y) = ---------
              gcd(x, y)

Above we transform the problem of computing the LCM into the problem of
computing the GCD. Next, observe that lcm(x,y,z) ≡ lcm(lcm(x,y),z), thus we can
use reduce to apply LCM to the numbers from 1 to 20 and get to our result.

'''


class Euler(BaseEuler):
    def solve(self):
        lcm = lambda x, y: x * y // gcd(x, y)
        res = reduce(lcm, range(1, 21))
        print('The smallest positive number that is evenly divisible\n' +
              'by all of the numbers from 1 to 20 is: %d' % res)

    @property
    def problem(self):
        return '''
Project Euler Problem 5:

   2520 is the smallest number that can be divided by each of the
   numbers from 1 to 10 without any remainder.

   What is the smallest positive number that is evenly divisible
   by all of the numbers from 1 to 20?
'''
