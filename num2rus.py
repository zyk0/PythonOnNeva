#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
num2rus.py: Convert numbers to Russian words. Return result in rubles
"""

__author__ = "Viacheslav Shvets"
__version__ = "0.1"
__email__ = "slava@shvec.com"

import sys

basic_words = ((u'', u'', u'', u'десять'),
               (u'один', u'', u'сто', u'одиннадцать'),
               (u'два', u'двадцать', u'двести', u'двенадцать'),
               (u'три', u'тридцать', u'триста', u'тринадцать'),
               (u'четыре', u'сорок', u'четыреста', u'четырнадцать'),
               (u'пять', u'пятьдесят', u'пятьсот', u'пятнадцать'),
               (u'шесть', u'шестьдесят', u'шестьсот', u'шестнадцать'),
               (u'семь', u'семьдесят', u'семьсот', u'семнадцать'),
               (u'восемь', u'восемьдесят', u'восемьсот', u'восемнадцать'),
               (u'девять', u'девяносто', u'девятьсот', u'девятнадцать'))

measurement_units = ((False, u'рубль', u'рубля', u'рублей'),
                     (True, u'тысяча', u'тысячи', u'тысяч'),
                     (False, u'миллион', u'миллиона', u'миллионов'),
                     (False, u'миллиард', u'миллиарда', u'миллиардов'),
                     (False, u'триллион', u'триллиона', u'триллионов'))


def num2rus(number):
    if (len(str(number)) > len(measurement_units) * 3):
        raise ValueError('Number too big')
    # If the number is zero, the solution is very simple:
    if number == 0:
        return u'Ноль %s' % measurement_units[0][3]  # That's all!
    # Initialize empty unicode string for result
    result = u""
    # Begin the loop
    for i, unit in enumerate(measurement_units):
        # Divide the number into 2 parts: triplet (last three digits) and other
        number, triplet = divmod(number, 1000)
        # If the triplet is zero, then iteration will pass:
        if triplet == 0:
            # If it's the first iteration, then assign the first basic unit
            if i == 0:
                result = unit[3]
            continue

        # Initialize empty unicode string for temporary triplet result
        preresult = u""
        # Define gender var. True - female, False - male, None - neuter
        female = unit[0]
        # Just mod 10 of triplet
        mod10 = triplet % 10

        i = 0  # reset iterator for internal loop, coming soon

        # Define wordform for measurement unit
        if mod10 == 1:
            wordform = unit[1]
        elif mod10 in range(2, 5):
            wordform = unit[2]
        else:
            wordform = unit[3]

        # If the second digit in the range 1..9, then special case:
        if triplet % 100 in range(10, 20):
            preresult = ' %s%s' % (basic_words[triplet % 10][3], preresult)
            triplet /= 100
            i = 2  # pass 2 iteration in next loop (tens, hundreds)
            wordform = unit[3]

        while i < 3:
            preresult = ' %s%s' % (basic_words[triplet % 10][i], preresult)
            triplet /= 10
            i += 1
        else:
            # Post-processing in the preresult, change a suffix
            if mod10 == 1 and female is None:
                preresult = preresult[:-2] + u'но'
            elif mod10 == 1 and female:
                preresult = preresult[:-2] + u'на'
            elif mod10 == 2 and female:
                preresult = preresult[:-1] + u'е'

        # Merge the resulting values ​​with those of the previous triplets
        result = '%s %s %s' % (preresult, wordform, result)
        # Trim double spaces and make the first letter is capitalized
        result = " ".join(result.split()).capitalize()

    return result


def main():
    try:
        number = int(sys.argv[1])
    except ValueError:
        print 'The argument is not integer. Please give a integer number'
    except:
        print 'No argument. Please give a integer number. Example: 23564576'
    else:
        print u'Число %s в рублях:\n%s' % (number, num2rus(number))


if __name__ == '__main__':
    main()
