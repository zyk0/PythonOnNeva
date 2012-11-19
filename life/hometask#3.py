#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Build_area():

    empty_sell =' '
    sell = 'X'

    def __init__(self, width, height):

        self.width = width
        self.height = height

        line = [self.empty_sell for x in xrange(self.width)]
        self.area = [line for x in xrange(self.height)]



if __name__ == '__main__':
    #Строим поле
    area = Build_area(20,20)
