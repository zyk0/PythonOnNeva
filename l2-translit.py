# -*- coding: utf-8 -*-

def makemap(fromstr, tostr):
    """makemap(frm, to) -> dict

    Return a transliteration map (a dictionary).
    The strings frm and to must be of the same length.

    """
    if len(fromstr) != len(tostr):
        raise ValueError, "makemap arguments must have same length"
    transmap = {}
    for i, (fromchar, tochar) in enumerate(zip(fromstr, tostr)):
        if tochar == " ":
            tochar = ""
        if fromchar == " ":
            while fromstr[i] == " ":
                i -= 1
            transmap[fromstr[i]] += tochar
        else:
            transmap[fromchar] = tochar
    return transmap

def transliterate(string, transmap):
    """transliterate(string, transmap) -> string

    Return a string transliterated in transmap format.

    """
    transliterated_string = ""
    for char in string:
        if char in transmap.keys():
            char = transmap[char]
        elif char.lower() in transmap.keys():
            char = transmap[char.lower()]
            char = char[0].upper() + char[1:]
        transliterated_string += char
    return transliterated_string

# Как в паспорте
mvd = makemap(u"абвгдеё ж зийклмнопрстуфхц ч ш щ   ъыьэю я ",
              u"abvgdeyozhziyklmnoprstufhtschshshch y eyuya")

# Устаревший ГОСТ
gost16876 = makemap(u"абвгдеё ж зий клмнопрстуфх цч ш щ  ъ ыьэ ю я ",
                    u"abvgdejozhzijjklmnoprstufkhcchshshh``y`ehjuja")

# Греческий стандарт
iso843 = makemap(u"αάβγδεέζηθ ιίϊκλμνξοόπρσςτυύϋφχ ψ ωώ",
                 u"aávgdeézīthiíïklmnxoóprsstyýÿfchpsōṓ")

sampletext1 = u"Уважаемый абонент! Через 50МБ скорость интернета будет ограничена"
sampletext2 = u"""
Стул — мебельное изделие для сидения одного человека, со спинкой,
с подлокотниками или без них, с высотой сиденья, функционально
удобной при соотношении его с высотой стола.

Аналогичная мебель без спинки называется табуретом. Основные части стула —
сиденье и спинка, в типичном стуле сиденье опирается на четыре ножки, иногда
в конструкцию стула входят подлокотники. Стул повышенной комфортности с
подлокотниками может называться креслом. Мебель для сидения двоих или более
людей именуется скамья, софа или диван. Для того, чтобы комфортно вытянуть
ноги, иногда употребляют пуфы.
"""
sampletext3 = u"""
Καρέκλα

Η καρέκλα είναι ένα καθιστικό έπιπλο.

Το ύψος του καθίσματος είναι συνήθως 42 έως 48 πόντους και κατάλληλο για
τραπεζαρία. Η προέλευση της καρέκλας και της πολυθρόνας είναι ο θρόνος.
Αρχικά, οι περισσότερες καρέκλες ήταν κατασκευασμένες από ξύλο, αλλά οι
σύγχρονες καρέκλες συνήθως είναι από μεταλλικούς σωλήνες η χυτό αλουμίνιο,
ενώ υπάρχουν και από διάφορα είδη πλαστικών.

Ως αντικείμενο στον βιομηχανικό σχεδιασμό είναι ένα από τα δημοφιλέστερα
και πολλοί σχεδιαστές και αρχιτέκτονες έχουν σχεδιάσει καρέκλες.
"""

print u"МВД: " + transliterate(sampletext1, mvd)
print u"ГОСТ 16876: " + transliterate(sampletext2, gost16876)
print u"ISO 843: " + transliterate(sampletext3, iso843)
