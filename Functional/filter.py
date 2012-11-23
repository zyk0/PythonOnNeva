#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# __author__ = "Alexander Ivanitsa"
# __version__ = "0.1"
# __email__ = "@"
#
# This is my realization FILTER function
#


def myfilter(func, *args):
    for item in range(len(args[0])):
        if func(item): yield item

if __name__ == '__main__':
    x2 = list(myfilter(lambda x: x % 2, xrange(18000000)))
    x1 = list(filter(lambda x: x % 2, xrange(18000000)))
    # print x1
    # print x2
