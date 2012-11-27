#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
gameoflife.py: The Game of Life, also known simply as Life.

* Generates random area by given size.
* User can limit the number of steps.

This is a training lesson. Script hasn't been tested.
"""

__author__ = "Viacheslav Shvets"
__version__ = "0.1"
__email__ = "slava@shvec.com"

import sys
import time
import random
import getopt

class Life():
    def __init__(self, alive):
        if type(alive) is not bool:
            raise ValueError('The argument is not boolean.')

        self.alive = alive
        self.neighbours = 0

    def __nonzero__(self):
        return self.alive

    def kill(self):
        self.alive = False

    def animate(self):
        self.alive = True

class Area():
    def __init__(self, width, height, max, sign_alive, sign_dead):
        self.wigth = width
        self.height = height
        self.max = max
        self.lifes = 0
        self.sign_alive = sign_alive
        self.sign_dead = sign_dead

        result = []
        for y in range(height):
            temp = []
            for x in range(width):
                alive = bool(random.getrandbits(1))
                temp += [ Life(alive) ]
            result += [ temp ]
        self.matrix = result

    def count_neighbours(self):
        m = self.matrix
        for x, row in enumerate(self.matrix):
            for y, cell in enumerate(row):
                result = bool(m[x - 1][y - 1]) + \
                         bool(m[x - 1][y]) + \
                         bool(m[x - 1][(y + 1) % len(row)]) + \
                         bool(m[x][y - 1]) + \
                         bool(m[x][(y + 1) % len(row)]) + \
                         bool(m[(x + 1) % len(m)][y - 1]) + \
                         bool(m[(x + 1) % len(m)][y]) + \
                         bool(m[(x + 1) % len(m)][(y + 1) % len(row)])
                cell.neighbours = result

    def next_step(self):
        self.lifes = 0
        for row in self.matrix:
            for cell in row:
                if cell.neighbours == 3 or (cell.neighbours ==2 and cell.alive):
                    cell.animate()
                else:
                    cell.kill()
                self.lifes += bool(cell)

    def display(self):
        for row in self.matrix:
            for cell in row:
                if bool(cell):
                    sys.stdout.write(self.sign_alive)
                else:
                    sys.stdout.write(self.sign_dead)
            sys.stdout.write('\n')
        sys.stdout.write('\n')

def usage():
    print """
    -w --width                Width of area
    -h --height               Height of area
    -m --max                  Maximum steps
    """

def main(width=20, height=10, max=100):
    try:
        opts, args = getopt.getopt(sys.argv[1:], "w:h:m:", ["width", "height",
                                                            "max"])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-w", "--width"):
            width = int(a)
        elif o in ("-h", "--height"):
            height = int(a)
        elif o in ("-m", "--max"):
            max = int(a)
        else:
            assert False, "unhandled option"

    try:
        sign_alive = u'☻'
        sign_dead = u'·'
        step_time = 0.3

        area = Area(width, height, max, sign_alive, sign_dead)

        for step in range(area.max):
            area.display()
            area.count_neighbours()
            area.next_step()
            time.sleep(step_time)
            sys.stdout.flush()

            if not area.lifes:
                area.display()
                print u'Эволюция завершилась. Все погибли.'
                break
            print '%d / %d' % (step, area.max)

            for i in range(area.height + 2):
                sys.stdout.write("\033[F")
                sys.stdout.flush()

        else:
            for i in range(area.height + 1):
                sys.stdout.write("\033[E")
            print u'Богам стало скучно. Эволюция идет слишком долго.'
            print u'Максимальное количество шагов: %d' % \
                area.max
            print u'Осталось в живых: %d' % area.lifes
    except ValueError, e:
        print e
        sys.exit(2)
    except KeyboardInterrupt, e:
        print u' Эволюция прервана. Последний шаг: %d' % step
        print u'Осталось в живых: %d' % area.lifes
        sys.exit(2)

if __name__ == '__main__':
    main()
