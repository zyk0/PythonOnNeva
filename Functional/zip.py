#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# __author__ = "Alexander Ivanitsa"
# __version__ = "0.1"
# __email__ = "@"
#
# This is my realization ZIP function
#


def myzip(*args):
    minlen = len(args[0])
    for item in args: minlen = min(minlen, len(item))

    for i in xrange(minlen):
        arg = []
        for item in args:
            arg.append(item[i])
        yield tuple(arg)

if __name__ == '__main__':
    x2 = list(myzip(range(2500000), range(1500000), range(1900000)))
    x1 = list(zip(range(1500000), range(25000000), range(19000000)))
    # print x2
    # print x1
