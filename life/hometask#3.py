#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep

class Board:
    cell  = 'X'
    blank = ' '

    def __init__(self, (width, height)):
        self.content = []
        self.width = width
        self.height = height
        self.near_cell = [(1, 0), (-1, 0), (1, 1), (-1, 1), (0, 1), (0, -1), (-1, -1), (1, -1)]

        for y in xrange(height):
            self.content.append([self.blank for x in xrange(width)])

    def in_bounds(self, (x, y)):
        if 0 <= x < self.width:
            if 0 <= y < self.height:
                return True
            else:
                return False
        else:
            return False

    def find_near_cell(self, (x, y)):
        neighbours = [(x + dx, y + dy) for dx, dy in self.near_cell]

        return filter(self.in_bounds, neighbours)

    def is_cell(self, (x, y)):
        return self.content[y][x] == self.cell

    def add(self, (x, y)):
        self.content[y][x] = self.cell

    def add_many(self, *seq):
        for position in seq: self.add(position)

    def add_predicate(self, predicate):
        for position in self.coordinates():
            if predicate(position):
                self.add(position)

    def remove(self, (x, y)):
        self.content[y][x] = self.blank

    def is_alive(self, position):
        n = len(filter(self.is_cell, self.find_near_cell(position)))
        if n == 3:
            return True
        elif self.is_cell(position):
            if 2 <= n <= 3:
                return True
            else:
                return False
        else:
            return False


    def coordinates(self):
        for x in xrange(self.width):
            for y in xrange(self.height):
                #return x, y
                yield x, y

    def next_step(self):
        births, deaths = [], []

        for position in self.coordinates():
            if self.is_alive(position):
                if not self.is_cell(position):
                    births.append(position)
            elif self.is_cell(position):
                deaths.append(position)

        for cell in births:
            self.add(cell)

        for cell in deaths:
            self.remove(cell)

    def __repr__(self):
        #for row in self.content:

        return "\n".join(" ".join(cell for cell in row) for row in self.content)

def build_field():
    field = Board((45, 20))

    # Планерное ружьё
    #-------------------------------------------------------------------------------------------------------
    #Блок
    field.add_many((3, 8), (4, 8), (3, 7), (4, 7))
    #Улий
    field.add_many((16, 5), (15, 6), (14, 7), (14, 8),(14, 9), (15, 10),
        (16, 11), (17, 10), (18, 9), (18, 8), (18, 7), (17, 6),
        (19, 9), (19, 8), (19, 7))
    #Неведомая хрень
    field.add_many((28, 3), (28, 4), (27, 4), (26, 4), (25, 4), (26, 5), (27, 5), (25, 5), (24, 5),
        (27, 6), (24, 6), (25, 7), (26, 7), (27, 7), (24, 7),
        (28, 8), (25, 8), (27, 8), (26, 8),(28, 9))
    #Палка
    field.add_many((33, 7), (33, 8))
    #Блок2
    field.add_many((37, 5), (37, 6), (38, 5), (38, 6))
    #-------------------------------------------------------------------------------------------------------

    return field

if __name__ == '__main__':
    field = build_field()
    print field
    raw_input("press enter")
    for i in xrange(1, 501):
        field.next_step()
        sleep(0.1)
