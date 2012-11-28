#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
        self.count = 0

    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(*args, **kwargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        self.count += 1
        print self.func.__name__, elapsed, self.alltime, self.count
        return result

@timer
def foo(n):
    return [x**10 for x in range(n)]
 
@timer
def foo2(n):
    return n**1000000
   
foo(1000)  
foo(2000)  
foo(3000)  

foo2(3)

foo(2500)
