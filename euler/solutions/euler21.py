# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.util import sum_of_divisors


class Euler(BaseEuler):
    def solve(self):
        res = sum([x for x in range(0, 10000)
                   if x == sum_of_divisors(sum_of_divisors(x))
                   and x != sum_of_divisors(x)])
        print('The sum of all the amicable numbers under 10000 is: %d' % res)

    @property
    def problem(self):
        return '''
Project Euler Problem 21:

    Let d(n) be defined as the sum of proper divisors of n (numbers less than n
    which divide evenly into n).

    If d(a) = b and d(b) = a, n a  b, then a and b are an amicable pair and
    each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
    55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
    71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
'''
