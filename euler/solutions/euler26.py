# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def solve(self):
        res, lgt = 0, (0, 0)
        for n in range(1, 1000):
            res = self._cycle_len(n)
            if res > lgt[1]:
                lgt = (n, res)

        return lgt[0]

    def _cycle_len(self, n):
        rl, ql, r = [], 0, 1
        while r:
            r = r % n
            if r in rl:
                return ql - rl.index(r)
            rl.append(r)
            r *= 10
            ql += 1
        return 0

    @property
    def answer(self):
        return ('The value of d < 1000 for which 1/d contains the longest\n' +
                'recurring cycle in its decimal fraction part is: %d'
                % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 26:

    A unit fraction contains 1 in the numerator. The decimal representation of
    the unit fractions with denominators 2 to 10 are given:

    1/2 =  0.5
    1/3 =  0.(3)
    1/4 =  0.25
    1/5 =  0.2
    1/6 =  0.1(6)
    1/7 =  0.(142857)
    1/8 =  0.125
    1/9 =  0.(1)
    1/10 =  0.1

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
    be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring
    cycle in its decimal fraction part.
'''
