#!/usr/bin/env python
#-*- coding: UTF-8 -*-
# Задача: напишите функцию, которая принимает на вход текущее время в часах и
# если это интервал между 10 и 16 - тогда сделайте скидку 20%
# В данном скрипте принцип немного другой. На вход принимается сумма, от которой будет считаться
# скидка. И если сейчас акционное время, выводится сумма со скидкой.
import sys
import datetime


def test_time():
    # Create datetime objects
    now = datetime.datetime.now()
    discount_begin = now.replace(hour=10, minute=0, second=0, microsecond=0)
    discount_end = now.replace(hour=16, minute=0, second=0, microsecond=0)

    # Test time
    if now < discount_begin:
        print 'Акция ещё не началась. До начала:', discount_begin - now
        return 0
    else:
        if now >= discount_end:
            print 'Акция закончилась. С того момента прошло:', now - discount_end
            print 'Следующая акция завтра'
            return False
        return True

if __name__ == '__main__':
    try:
        sum = sys.argv[1]
    except:
        print 'Сумма не задана'
        if test_time() is True:
            print 'Акция вовсю идёт. Укажите в параметре сумму и будет посчитана скидка'
    else:
        if test_time() is True:
            try:
                result_sum = float(sum) * 0.8
            except:
                print 'Не удалось посчитать. Но акция действует'
            else:
                print 'Стоимость со скидкой 20%:', result_sum
