#!/usr/bin/env python
'''
Conway's Game of Life

Ever row - 1 int
Ever bit - 1 cell
'''


from random import randrange
from string import maketrans


class BaseLife(object):
    def __init__(self, width=24, height=8):
        ''' Initialize the board by default'''
        self.width = width
        self.height = height
        self._aGrid = []
        for i in range(height):
            self._aGrid.append(randrange(1 << width))

    def __getitem__(self, pos):
        ''' self[x, y] -> bit '''
        if type(pos) != tuple or len(pos) != 2:
            raise IndexError('Index must be a tuple of length 2')
        x, y = pos
        if 0 <= x < self.width and 0 <= y < self.height:
            return (self._aGrid[y] & (1 << x)) >> x
        else:
            raise IndexError('Grid index out of range')

    def __setitem__(self, pos, value):
        ''' self[x, y] = bit (1/0) '''
        if type(pos) != tuple or len(pos) != 2:
            raise IndexError('Index must be a tuple of length 2')
        x, y = pos
        if 0 <= x < self.width and 0 <= y < self.height:
            if value:
                self._aGrid[y] = self._aGrid[y] | (1 << x)  # set bit x to 1
            else:
                self._aGrid[y] = self._aGrid[y] & ~(1 << x)  # set bit x to 0
        else:
            raise IndexError('Grid index out of range')

    def printLife(self):
        ''' Print current state '''
        fillCharakter = " "
        for y in range(self.height):
            s1 = fillCharakter * self.width
            table = maketrans('01', fillCharakter + '*')
            s2 = bin(self._aGrid[y])[2:].translate(table)
            print s1[:len(s1) - len(s2)] + s2

    def countLiveCell(self, data, xpos):
        ''' Counting bits in a row '''
        mask = (1 << self.width) - 1  # 111...11111  width == self.width
        data = data & mask            # Cleaning excess bits
        if xpos:
            data = (data >> (xpos - 1)) & 7
        else:
            data = data & 3

        if not data:
            return 0
        if data == 3 or data == 5 or data == 6:
            return 2
        if data == 1 or data == 2 or data == 4:
            return 1
        return 3

    def nextStep(self):
        ''' calculation of the next step '''
        aTempGrid = tuple(self._aGrid)
        for y in range(self.height):
            for x in range(self.width):
                liveCell = 0
                # Top
                if y != 0:
                    liveCell += self.countLiveCell(aTempGrid[y - 1], x)
                # Clear bit with calculation cell
                liveCell += self.countLiveCell(aTempGrid[y] & ~(1 << x), x)
                # Bottom
                if y < self.height - 1:
                    liveCell += self.countLiveCell(aTempGrid[y + 1], x)

                if liveCell == 3:
                    self[x, y] = 1
                if liveCell < 2 or liveCell > 3:
                    self[x, y] = 0

if __name__ == "__main__":
    f = BaseLife(50, 20)

    # For test
#    for y in range(f.height):
#        f._aGrid[y] = 0
#    f._aGrid[1] = 2 << 40
#    f._aGrid[2] = 1 << 40
#    f._aGrid[3] = 7 << 40
#    f.printLife()

    while True:
        print "=" * f.width
        f.nextStep()
        f.printLife()
        raw_input("Next? ")
