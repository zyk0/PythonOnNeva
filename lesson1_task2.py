#!/usr/bin/env python
#-*- coding: UTF-8 -*-
# Задача: Перебрать кортеж чисел, если число четное - возвести в квадрат и
# добавить в выходной список


def sort_numbers(numbers):
    return [number * number for number in numbers if number % 2 is 0]


if __name__ == "__main__":
    base_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print sort_numbers(base_numbers)
