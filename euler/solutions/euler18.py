# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


'''
This is a really interesting problem and the solution is really simple and
clever.  The solution takes from graph theory. See notes below for details.
Doing a brute force search on the triangle in this problem works fine but it's
not optimal. Problem 67 is basically the same problem as this one, but the
input data is too large for brute force. I need a clever algorithm...

'''


EULER_DATA = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


def get_triangle(data):
    '''
    I want to represent the data as a List of List of Int so I break the data
    down by line and then by space and convert it to Int and return the data
    structure.
    '''
    return [[int(num) for num in line.split()]
            for line in data.split('\n')]


def find_max_sum(tri):
    '''
    We keep reducing the triangle until there is only one item left
    and that's our result.
    '''
    while len(tri) > 1:
        tri = reduce_triangle(tri)

    return tri[0][0]


def reduce_triangle(tri):
    '''
    The key strategy of the algorithm is to treat the data from the bottom up.
    Here are the steps:

     1. Get the last row of the triangle
     2. Get the next to the last row of the triangle
     3. Loop through the items from step 2 above
     4. Find the 2 adjacent items for the item in step 3 above
     5. Select the largest of the 2 items from step 4 above
     6. Replace the item in step 3 above with the sum of item in step 5
        and the original item from step 3
     7. Remove the last row from the triangle

    This is a form of reduction because the next to the last row will contain
    the accumulation of the items values after each iteration of the loop in
    find_max_sum
    '''
    lastrow = tri[-1]

    for index in range(0, len(tri) - 1):
        tri[-2][index] += max(lastrow[index:index + 2][0],
                              lastrow[index:index + 2][1])

    tri.pop()
    return tri


class Euler(BaseEuler):
    def solve(self):
        print('The maximum sum travelling from the top of the triangle to ' +
              'the base is: %d' % find_max_sum(get_triangle(EULER_DATA)))

    @property
    def problem(self):
        return '''
Project Euler Problem 18:

    By starting at the top of the triangle below and moving to adjacent numbers
    on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:
%s
''' % EULER_DATA
