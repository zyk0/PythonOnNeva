# -*- coding: utf-8 -*-
import datetime

def sale_at_10_16():
    'Получим текущий час'
    hour_now = datetime.datetime.now().strftime('%H')

    'Сумма чека'
    summ = (int(raw_input('Введите сумму:')))

    if (10 < hour_now > 16):
        summ = summ - summ * 20 / 100
        print ('Сумма со скидкой равна:'), summ
    else:
        print('Сумма равна:'), summ


if __name__ == '__main__':
    sale_at_10_16()