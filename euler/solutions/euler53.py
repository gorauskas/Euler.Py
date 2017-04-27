# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def solve(self):
        maxn, L, num, prev = 100, 1000000, 0, [1, 1]

        for i in range(2, maxn + 1):
            new = [1]
            for i, c1 in enumerate(prev[:-1]):
                c2 = prev[i + 1]
                c = c1 + c2
                if c > L:
                    num += 1
                new.append(c)
            new.append(1)
            prev = new[:]
        return num

    @property
    def answer(self):
        return ('There are %d values greater than one million.' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 53

    There are exactly ten ways of selecting three from five, 12345:

        123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

                                           5
    In combinatorics, we use the notation,  C = 10.
                                             3

    In general,

        n         n!
         C  = ----------   where r <= n, n! = n*(n−1)*...*3*2*1, and 0! = 1.
          r    r!(n−r)!

                                                              23
    It is not until n = 23, that a value exceeds one-million:   C   = 1144066.
                                                                 10

                                                  n
    How many, not necessarily distinct, values of  C , for 1 <= n <= 100,
                                                    r
    are greater than one-million?
'''
