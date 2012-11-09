# -*- coding: utf-8 -*-
"Напишите функцию траслитирования русского текста."

def translit(MyString):
    """
    Эта функция переводит строку MyString в транслит
    """
    #Создадим списки c алфавитом

    strRu = u'а,б,в,г,д,е,ё,ж,з,и,й,к,л,м,н,о,п,р,с,т,у,ф,х,ц,ш,щ,ъ,ы,ь,э,ю,я'

    strLat = u'A,B,V,G,D,E,Jo,Zh,Z,I,J,K,L,M,N,O,P,R,S,T,U,F,H,C,Sh,W,#,Y,*,Je,Ju,Ja'

    listRu = strRu.split(",")

    listLat = strLat.split(",")

    newString = ""

    for letter in MyString:
        try:
            #Найдем наш символ в списке listRu
            indexList = listRu.index(letter)
            #Проверка на заглавные буквы
            if letter.islower():
                newString = newString + listLat[indexList].lower()
            else:
                newString = newString + listLat[indexList]
        except:
            #Если  ощибка тогда это либо пробел либо символ отсутствующий в списке
            newString = newString + letter

    return newString

if __name__ == '__main__':
    print translit(u'Съеште ещё этих сладких француских булок')
