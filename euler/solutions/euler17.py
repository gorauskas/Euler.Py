# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


def lookup_table():
    d = {}
    d[1] = 'one'
    d[2] = 'two'
    d[3] = 'three'
    d[4] = 'four'
    d[5] = 'five'
    d[6] = 'six'
    d[7] = 'seven'
    d[8] = 'eight'
    d[9] = 'nine'
    d[10] = 'ten'
    d[11] = 'eleven'
    d[12] = 'twelve'
    d[13] = 'thirteen'
    d[14] = 'fourteen'
    d[15] = 'fifteen'
    d[16] = 'sixteen'
    d[17] = 'seventeen'
    d[18] = 'eighteen'
    d[19] = 'nineteen'
    d[20] = 'twenty'
    d[30] = 'thirty'
    d[40] = 'forty'
    d[50] = 'fifty'
    d[60] = 'sixty'
    d[70] = 'seventy'
    d[80] = 'eighty'
    d[90] = 'ninety'
    d[100] = 'hundred'
    d[1000] = 'thousand'
    return d


def spell_number(n):
    buff = []
    t = lookup_table()
    num = [int(y) for y in reversed([x for x in str(n)])]

    if len(num) == 4 and num[3] != 0:
        buff.append(t[num[3]] + ' thousand')

    if len(num) >= 3 and num[2] != 0:
        buff.append(t[num[2]] + ' hundred')
        if len(num) >= 2 and num[1] != 0:
            buff.append(' and')
        elif len(num) >= 1 and num[0] != 0:
            buff.append(' and')

    dpv = 99
    if len(num) >= 2 and num[1] != 0:
        dpv = num[1] * 10 + num[0]
        if dpv <= 20:
            buff.append(' ' + t[dpv])
        else:
            buff.append(' ' + t[num[1] * 10])

    if len(num) >= 1 and num[0] != 0 and dpv > 20:
        buff.append(' ' + t[num[0]])

    return ''.join(buff).replace(' ', '')


class Euler(BaseEuler):
    def solve(self):
        res = [spell_number(x) for x in range(1, 1001)]
        print('The numbers from 1 to 1000, when written out in words, ' +
              'have %d letters.' % len(''.join(res).replace(' ', '')))

    @property
    def problem(self):
        return '''
Project Euler Problem 17:

    If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written
    out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of 'and' when writing out numbers is in compliance
    with British usage.
'''
