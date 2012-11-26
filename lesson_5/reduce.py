#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
reduce.py: This is my realization the built-in reduce() function.
"""

__author__ = "Viacheslav Shvets"
__version__ = "0.1"
__email__ = "slava@shvec.com"

def my_reduce(function, iterable, initializer=None):
	iterator = iter(iterable)

	if initializer is not None:
		result = initializer
	else:
		result = next(iterator)
	for x in iterator:
		result = function(result, x)
	return result


###############################################################################

# Tests

numbers = xrange(1, 10)

def spam(x, y):
	return x * y

reduce(spam, numbers, 10)
# 3628800
my_reduce(spam, numbers, 10)
# 3628800

reduce(spam, numbers)
# 362880
my_reduce(spam, numbers)
# 362880

###############################################################################

# Profiling (-m cProfile)

reduce(spam, xrange(100000), 10)
my_reduce(spam, xrange(100000), 10)
"""
         200046 function calls in 10.367 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   200034    5.238    0.000    5.238    0.000 reduce.py:24(spam)
        1    0.000    0.000   10.367   10.367 reduce.py:3(<module>)
        3    2.475    0.825    5.022    1.674 reduce.py:3(my_reduce)
        3    0.000    0.000    0.000    0.000 {iter}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {next}
        3    2.653    0.884    5.344    1.781 {reduce}
"""