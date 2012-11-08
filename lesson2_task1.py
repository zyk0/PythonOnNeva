#!/usr/bin/env python
#-*- coding: UTF-8 -*-
# Задача: Напишите функцию траслитирования русского текста.
# Реализовано на хэшах
# Еще можно на кортежах, 2 кортежа, совмещать по индексам
# Интересно, что быстрее

import sys

translit_chars = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
                  'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
                  'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                  'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
                  'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '"', 'ы': 'y', 'ь': "'",
                  'э': 'e', 'ю': 'yu', 'я': 'ya',
                  'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
                  'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K',
                  'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
                  'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts',
                  'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '"', 'Ы': 'Y', 'Ь': "'",
                  'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'}


def convert_string(string):
    # Если все возможные символы текста известны и их внести в хэш-таблицу,
    # можно сделать так)):
    #converted_string = (translit_chars[char.encode('utf-8')]
                        #for char in string.decode('utf-8')
                        #if char.encode('utf-8') in translit_chars)
    #return ''.join(converted_string)

    converted_string = ''
    for char in string.decode('utf-8'):
        char = char.encode('utf-8')
        converted_string += translit_chars[char] if char in translit_chars else char
    return converted_string

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'Передайте в качестве параметра строку'
        exit()

    print convert_string(sys.argv[1])
