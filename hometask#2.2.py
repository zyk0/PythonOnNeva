# -*- coding: utf-8 -*-

def SummProp(l):
    #Тысячи
    Unit_tho = u'тысяча ,    тысячи ,    тысяч'
    #Миллион
    Unit_mil = u'миллион ,   миллиона ,  миллионов'
    #Миллиард
    Unit_mrd = u'миллиард ,  миллиарда , миллиардов'
    #Трилион
    Unit_tri = u'трилион ,   трилиона , трилионов'


    # Перенесом в строки в списки
    # при этом удалим все не нужные пробелы в списках
    list_Unit_tho = Unit_tho.replace(' ','').split(',')
    list_Unit_mil = Unit_mil.replace(' ','').split(',')
    list_Unit_mrd = Unit_mrd .replace(' ','').split(',')
    list_Unit_tri = Unit_tri.replace(' ','').split(',')

    s = ""
    s1= ""

    if l>=1000000000000:
        s1, momo = collect(l / 1000000000000,0)
        s+=" "+list_Unit_tri[momo]
        l = l%1000000000

    if l>=1000000000:
        s1, momo = collect(l / 1000000000,0)
        s+=" "+ s1 + " " +list_Unit_mrd[momo]
        l = l%1000000000

    if l>=1000000:
        s1, momo = collect(l / 1000000,0)
        s+=" "+ s1 + " " + list_Unit_mil[momo]
        l =l%1000000

    if l>=1000:
        if 999 < l < 2990:
            mo=1
        else:
            mo=0
        s1, momo = collect(l / 1000,mo)
        s+=" "+ s1 + " " +list_Unit_tho[momo]
        l=l%1000

    if l>=1:
        s1, momo = collect(l,0);

        s+=" "+s1;

    return s

def collect(i,mo):
    #Еденицы
    Unit_1_2  = u'одна ,    две'
    #Еденицы
    Unit_1_19 = u'один ,    два ,'\
                u'три  ,    четыре,'\
                u'пять ,    шесть,'\
                u'семь ,    восемь,'\
                u'девять ,  десять,'\
                u'одиннадцать ,     двенадцать,'\
                u'тринадцать ,      четырнадцать,'\
                u'пятнадцать ,      шестнадцать,'\
                u'семнадцать ,      восемнадцать,'\
                u'девятнадцать'
    #Десятки
    Unit_des = u'двадцать ,     тридцать,'\
               u'сорок ,        пятьдесят,'\
               u'шестьдесят ,   семьдесят,'\
               u'восемьдесят ,  девяносто'
    #Сотни
    Unit_hang = u'сто ,     двести,'\
                u'триста ,  четыреста,'\
                u'пятьсот , шестьсот,'\
                u'семьсот , восемьсот,'\
                u'девятьсот'

    resultword=""

    # Перенесом в строки в списки
    # при этом удалим все не нужные пробелы в списках
    list_Unit_1_2 = Unit_1_2.replace(' ','').split(',')
    list_Unit_1_19 = Unit_1_19.replace(' ','').split(',')
    list_Unit_des = Unit_des.replace(' ','').split(',')
    list_Unit_hang = Unit_hang.replace(' ','').split(',')

    if i>=100:
        resultword +=list_Unit_hang[i/100-1]
        i=i%100
    if i>19:
        resultword +=" "+list_Unit_des[i / 10-2]
        i=i%10
    if i!=0:
        if mo!=0:
            resultword +=" "+list_Unit_1_2 [i-1]
        else:
            resultword +=" "+list_Unit_1_19[i-1]
    momo =  {1 : 0,
            2 : 1,
            3 : 1,
            4 : 1}.get(i,2)


    return resultword, momo


if __name__ == '__main__':
    str = SummProp(1255478)
    print str

