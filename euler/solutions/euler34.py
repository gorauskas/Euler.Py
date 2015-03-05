# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


'''
These type of numbers are referred to as factorions and it’s easy to learn that
only 4 exist: 1, 2, 145 & 40585. The problem description wants us to ignore 1 &
2 so the answer to this problem should become obvious.

But, let’s write a program anyway to search for factorions. As usual, when
writing a brute force search algorithm, we must first determine our bounds. The
lower bound is 10 because single digit candidates are to be ignored. The upper
bound we discover as follows (from Wikipedia):

If n is a natural number of d digits that is a factorion, then
10d − 1 ≤ n ≤ 9!d and this fails to hold for d ≥ 8. Thus n has 7 digits and the
maximum sum of factorials of digits for a 7 digit number is 9!7 = 2,540,160,
which is the upper bound.

Afterwards, we learned 50,000 worked just fine.
'''


class Euler(BaseEuler):
    def solve(self):
        # pre-calc factorials from 1 to 9
        fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        r = 0  # results accumulator
        rng = range(10, 49989)

        for n in rng:
            x = sum([fact[int(d)] for d in str(n)])
            if n == x:
                r += n

        return r

    @property
    def answer(self):
        return ('The sum of all numbers which are equal to the sum of the ' +
                'factorial of\ntheir digits is %d' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 34:

    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the
    factorial of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
