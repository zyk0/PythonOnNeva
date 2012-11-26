#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
map.py: This is my realization the built-in map() function.
"""

__author__ = "Viacheslav Shvets"
__version__ = "0.1"
__email__ = "slava@shvec.com"

def my_zip_with_none(*args):
	"""
	By default, zip() function not returns None values, but my_map() function need that.
	So, in this function I fixed this using IndexError exception.
	"""
	minimum_length = len(max(args, key=len))
	result = [[] for i in xrange(minimum_length)]

	for arg in args:
		for i, list in enumerate(result):
			try:
				list.append(arg[i])
			except IndexError:
				list.append(None)

	return [tuple(x) for x in result]

def my_map(function, *args):
	result = []
	for args in my_zip_with_none(*args):
		result.append(function(*args))
	return result


###############################################################################

# Tests

a = [7, 2, 3, 10, 12]
b = [2, 1, -1, 4, 6]
c = [5, 4, 6, 9]

def spam(x, y):
	return x * y

map(spam, a, b)
# [14, 2, -3, 40, 72]

my_map(spam, a, b)
# [14, 2, -3, 40, 72]

def spam2(x, y, z):
	return x ** y, z

map(spam2, a, b, c)
# [(49, 5), (2, 4), (0.3333333333333333, 6), (10000, 9), (2985984, None)]

my_map(spam2, a, b, c)
# [(49, 5), (2, 4), (0.3333333333333333, 6), (10000, 9), (2985984, None)]

###############################################################################

# Profiling (-m cProfile)

map(lambda x, y: x*y, xrange(100000), xrange(100000))

my_map(lambda x, y: x*y, xrange(100000), xrange(100000))

def spam(x, y):
	if x is None:
		x = 0
	if y is None:
		y = 0
	return x + y

map(spam, xrange(130000), xrange(100000))

my_map(spam, xrange(130000), xrange(100000))
"""
         1150077 function calls in 58.103 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        4   11.514    2.879   46.441   11.610 map.py:20(my_map)
        1    0.012    0.012   58.103   58.103 map.py:3(<module>)
        4   12.354    3.089   23.666    5.917 map.py:3(my_zip_with_none)
       10    0.000    0.000    0.000    0.000 map.py:38(spam)
       10    0.001    0.000    0.001    0.000 map.py:47(spam2)
   100000    2.742    0.000    2.742    0.000 map.py:60(<lambda>)
   100000    2.605    0.000    2.605    0.000 map.py:62(<lambda>)
   260000    6.303    0.000    6.303    0.000 map.py:83(spam)
        4    0.000    0.000    0.000    0.000 {len}
        4    5.760    1.440   11.650    2.913 {map}
        4    0.000    0.000    0.000    0.000 {max}
   690035   16.811    0.000   16.811    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""