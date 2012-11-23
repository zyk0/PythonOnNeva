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
    for i in range(len(args[0])):
        arg = []
        for item in args:
            arg.append(item[i])
        yield tuple(arg)

if __name__ == '__main__':
    x2 = list(myzip(range(1500000), range(15000000), range(15000000)))
    x1 = list(zip(range(15000000), range(15000000), range(15000000)))
    # print x2
    # print x1
