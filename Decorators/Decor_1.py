#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import traceback


class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
        self.countstart = 0  # Счетчик вызовов декоратора

    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(*args, **kwargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        self.countstart += 1

        # Кол-во вызовов идет после имени функции
        print "===\n%s:%d, time: %f sec., alltime: %f sec." % \
        (self.func.__name__, self.countstart, elapsed, self.alltime)

        # traceback.extract_stack() - информация о стеке вызовов
        for item in traceback.extract_stack():
            if not "traceback" in item[3]:  # обрезать вызов собсвенно traceback
                print "line %s, string %s" % (item[1], item[3])
        return result


@timer
def foo(n):
    return [x ** 10 for x in range(n)]

def fooUP():
    foo(1000)

def fooUP2():
    fooUP()
    foo(2000)

def fooUP3():
    fooUP2()
    foo(3000)


foo(4000)
fooUP3()
