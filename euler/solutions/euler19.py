# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
import datetime as dt


class Euler(BaseEuler):
    def solve(self):
        res = 0

        for y in range(1901, 2001):
            for m in range(1, 13):
                if dt.date(y, m, 1).weekday() == 6:
                    res += 1

        print('There were %d Sundays falling on the first of the month in '
              % res + 'the twentieth century.')

    @property
    def problem(self):
        return '''
Project Euler Problem 19:

    You are given the following information, but you may prefer to do some
    research for yourself.

    a. 1 Jan 1900 was a Monday.
    b. Thirty days has September,
       April, June and November.
       All the rest have thirty-one,
       Saving February alone,
       Which has twenty-eight, rain or shine.
       And on leap years, twenty-nine.
    c. A leap year occurs on any year evenly divisible by 4, but not on a
       century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?
'''
