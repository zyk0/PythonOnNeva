#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
zip.py: This is my realization the built-in zip() function.
"""

__author__ = "Viacheslav Shvets"
__version__ = "0.1"
__email__ = "slava@shvec.com"

def my_zip(*args):
    minimum_length = len(min(args, key=len))
    result = [[] for i in xrange(minimum_length)]

    for arg in args:
        for i, list in enumerate(result):
            list.append(arg[i])

    return [tuple(x) for x in result]

###############################################################################

# Tests

a = [1, 2, 3, 11, 200]
b = [4, 5, 6, 12, 100]
c = [7, 8, 9, 13]
d = [4, 5, 5, 4, 43, 89]

print my_zip(a, b)
# [(1, 4), (2, 5), (3, 6), (11, 12), (200, 100)]

print my_zip(a, b, c)
# [(1, 4, 7), (2, 5, 8), (3, 6, 9), (11, 12, 13)]

print my_zip(a, b, d)
# [(1, 4, 4), (2, 5, 5), (3, 6, 5), (11, 12, 4), (200, 100, 43)]

###############################################################################

# Profiling (-m cProfile)

a = list(xrange(300000))
b = list(xrange(200000))
c = list(xrange(400000))

zip(a, b, c)

my_zip(a, b, c)
"""
         600052 function calls in 12.712 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.647    0.647   12.712   12.712 zip.py:3(<module>)
        4    6.609    1.652   11.201    2.800 zip.py:3(my_zip)
        4    0.000    0.000    0.000    0.000 {len}
   600037    4.588    0.000    4.588    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.004    0.001    0.004    0.001 {min}
        1    0.864    0.864    0.864    0.864 {zip}
"""
