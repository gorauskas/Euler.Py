# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def is_palindrome(self, n):
        return str(n) == str(n)[::-1]

    def solve(self):
        res = 0

        for x in range(100, 1000):
            for y in range(100, 1000):
                if self.is_palindrome(x * y) and (x * y) > res:
                    res = x * y

        return res

    @property
    def answer(self):
        return ('The largest palindrome made of the product of two ' +
                '3 digit numbers is %d' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 4:

   A palindromic number reads the same both ways. The largest palindrome made
   from the product of two 2-digit numbers is 9009 = 91  99.

   Find the largest palindrome made from the product of two 3-digit numbers.
'''
