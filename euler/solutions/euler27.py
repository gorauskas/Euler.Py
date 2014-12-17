# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.util import is_prime


class Euler(BaseEuler):
    def solve(self):
        max, res, a, b = 0, 0, 0, 0
        for x in range(-999, 1000):
            for y in range(-999, 1000):
                done = False
                count = 0
                while not done:
                    num = count * count + x * count + y
                    if num > 0 and is_prime(num):
                        count += 1
                    else:
                        done = True
                if count > max:
                    a, b, max, res = x, y, count, x * y

        print('A sequence of length %d, is generated by a=%d, b=%d, the product is %d'
              % (max, a, b, res))

    @property
    def problem(self):
        return '''
Project Euler Problem 27:

    Euler published the remarkable quadratic formula:

    n² + n + 41

    It turns out that the formula will produce 40 primes for the consecutive
    values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is
    divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
    divisible by 41.

    Using computers, the incredible formula  n² - 79n + 1601 was discovered,
    which produces 80 primes for the consecutive values n = 0 to 79. The
    product of the coefficients, -79 and 1601, is -126479.

    Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

    Find the product of the coefficients, a and b, for the quadratic
    expression that produces the maximum number of primes for consecutive
    values of n, starting with n = 0.
'''