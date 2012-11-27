#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
filter.py: This is my realization the built-in filter() function.
"""

__author__ = "Viacheslav Shvets"
__version__ = "0.1"
__email__ = "slava@shvec.com"

def my_filter(function, iterable):
    return [x for x in iterable if function(x)]


###############################################################################

# Tests

numbers = xrange(-10, 10)

def spam(x):
    return x > 5

my_filter(spam, numbers)
# [6, 7, 8, 9]

filter(spam, numbers)
# [6, 7, 8, 9]


###############################################################################

# Profiling (-m cProfile)

my_filter(spam, xrange(100000))

filter(spam, xrange(100000))
"""
         200046 function calls in 10.222 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   200040    5.055    0.000    5.055    0.000 filter.py:16(spam)
        1    0.005    0.005   10.222   10.222 filter.py:3(<module>)
        2    2.529    1.264    4.949    2.474 filter.py:3(my_filter)
        2    2.633    1.317    5.268    2.634 {filter}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""