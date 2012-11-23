#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# __author__ = "Alexander Ivanitsa"
# __version__ = "0.1"
# __email__ = "@"
#
# This is my realization MAP function
#


def mymap(func, *args):
    if len(args) == 1:
        print type(args[0])
        for i in args[0]: yield func(i)
    else:
        for i in range(len(args[0])):
            arg = []
            for item in args: arg.append(item[i])
            yield func(*arg)

if __name__ == '__main__':
    # print list(mymap(lambda x: x ** 3, [1, 2, 3, 4, 5, 6]))
    x2 = list(mymap(lambda x, y: x ** y, range(15000), range(15000)))
    x1 = list(map(lambda x, y: x ** y, range(15000), range(15000)))
    # print x1
    # print x2
