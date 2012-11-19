#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
        self.countstart = 0

    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(*args, **kwargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        self.countstart += 1
        print "%s:%d, time: %f sec., alltime: %f sec." % \
        (self.func.__name__, self.countstart, elapsed, self.alltime)
        return result


@timer
def foo(n):
    return [x ** 10 for x in range(n)]


foo(1000)
foo(2000)
foo(3000)
