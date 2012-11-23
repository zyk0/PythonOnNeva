#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# __author__ = "Alexander Ivanitsa"
# __version__ = "0.1"
# __email__ = "@"
#
# This is my realization REDUCE function
#


def myreduce(func, args, init=0):
    ret = func(init, args[0])
    for item in range(len(args) - 1):
        ret = func(ret, args[item + 1])
    return ret

if __name__ == '__main__':
    x2 = myreduce(lambda x, y: x * y, xrange(1, 130000), 1)
    x1 = reduce(lambda x, y: x * y, xrange(1, 130000), 1)
    # print x1
    # print x2
