#Создать класс Word, содержащий поле _word (строка) и _translations (переводы, set строк).
# Класс представляет объектное описание английского слова + его переводов на украинский.

class Word ():
    _word = ""
    _translations = ""

#- метод __init__, принимающий обязательным параметром word и опциональным - translations (по умолчанию - frozenset()).
    def __init__ (self,word, translations=frozenset('')):
        self._word=word
        self._translations= translations

#- метод __str__, возвращающий строку вида "wood - дерево, лiс"

    def __str__(self):
        if self._translations != frozenset():
            toSTR = self._word + ' - ' + self._translations
        else:
            toSTR = self._word + ' - '
        return toSTR

#- метод __add__, принимающий translation (строковое значение нового варианта перевода).
# Метод должен добавить перевод в существующее множество переводов.
    def __add__(self,translation):
        if self._translations != frozenset():
            self._translations = self._translations + ', ' + translation
        else:
            self._translations = translation
        return self._translations


#- метод __eq__, сравнивающий у объектов класса Word значения поля _word.
    def __eq__(self,other:"Word"):
        return self._word == other._word


#- метод __ne__, являющийся обращением метода __eq__
    def __ne__(self, other:"Word"):
        return not (self == other)

#--------проверка 1-го класса
w1 = Word('water','вода')
w1 + 'поливати'
print(w1)

w2 = Word('water')
print(w2)
w2 + 'вода'
print(w2)

w3 = Word('rain','дощ')
print(w3)

print (w1==w2)
print (w1==w3)
print (w1!=w2)

#--------------------

#2. Создать класс Vocabulary, описывающий словарь, состоящий из объектов класса Word.
# Объекты должны храниться во внутреннем словаре _words, где
# ключ - значение поля _word, значение - объект Word.

class Vocabulary (Word):
    _words ={}

#- __init__, без параметров
    def __init__(self):
        _words = {}
        super(Vocabulary, self).__init__(self)
        #self._words[id._word] = Word._translations
        #print(f"----   {_words}")

#- __add__, добавляющий объект Word в словарь.
    def __add__(self, other):
        self._words[other._word] = other._translations
#        print(self.super(Vocabulary, self)._word)
#        self._words[Word._word] = Word._translations
        print (self._words)
        return self._words

#- __getattribute__(word), возвращающий объект Word по ключу word, если word присутствует в словаре _words.
# В противном случае возвращает super().__getattribute__(word)

#- __setattr__ - добавляет слово в словарь (условия реализации см ниже в __setitem__)

#- __delattr__, удаляющий слово из словаря

#- __getitem__(word), возвращающий объект Word по ключу word из _words

#- __setitem__(word, value) - создающий новое слово в словаре.
# Если value - объект класса Word, то проверить соответствие word  и
# _word (бросить ValueError в случае несоотвествия).
# Если value - строка, то создать объект Word,
# используя value в качестве одного из переводов.

#- __len__ - возвращающий количество слов в словаре

#- __str__ - возвращающий строку вида "EN-UA Vocabulary (<количество> words)"

v1 = Vocabulary()
v1+w1
v1+w3
