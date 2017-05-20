# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def solve(self):
        pc, cl, n = {}, {}, 1

        while True:
            sd = int(''.join(sorted(str(n ** 3), reverse=True)))
            if sd in pc:
                pc[sd] += 1
                cl[sd].append(n)
                if pc[sd] == 5:
                    break
            else:
                pc[sd] = 1
                cl[sd] = [n]
            n += 1

        return cl[sd][0]**3

    @property
    def answer(self):
        return ('The smallest cube for which five permutations of its ' +
                'digits are cube is %d.' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 62

    The cube, 41063625 (3453), can be permuted to produce two other cubes:
    56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube
    which has exactly three permutations of its digits which are also cube.

    Find the smallest cube for which exactly five permutations of its digits
    are cube.
'''
