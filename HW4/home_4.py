#Create a Word class containing the _word (string) and _translations (translations, set strings) fields.
#The class represents an object description of an English word + its translations into Ukrainian.

class Word ():
    _word = ""
    _translations = ""

#- __init__ method accepting word as mandatory parameter and translations as optional parameter (by default - frozenset()).
    def __init__ (self,word, translations=frozenset('')):
        self._word=word
        self._translations= translations

#- __str__ method, returning a string of the form "wood - дерево, лiс"

    def __str__(self):
        if self._translations != frozenset():
            toSTR = self._word + ' - ' + self._translations
        else:
            toSTR = self._word + ' - '
        return toSTR

#__add__ method accepting translation (string value of the new translation variant).
# The method should add the translation to the existing set of translations.
    def __add__(self,translation):
        if self._translations != frozenset():
            self._translations = self._translations + ', ' + translation
        else:
            self._translations = translation
        return self._translations


#- __eq__ method comparing the values of the _word field in Word class objects.
    def __eq__(self,other:"Word"):
        return self._word == other._word


#-__ne__ method, which is an invocation of __eq__ method
    def __ne__(self, other:"Word"):
        return not (self == other)

#--------1st class inspection
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

#2.  Create a Vocabulary class describing a dictionary consisting of objects of the Word class.
# The objects should be stored in the internal dictionary _words, where
# key is the value of the _word field, value is a Word object.

class Vocabulary (Word):
    _words ={}

#- __init__, 
    def __init__(self):
        _words = {}

#- __add__, adding a Word object to the dictionary.
    def __add__(self, other):
#        self._words[other._word] = other
        return self.new_word(other._word,other)
#        return self._words

#- __getattribute__(word), returning a Word object by the word key if word is present in the _words dictionary.
# Otherwise returns super().__getattribute__(word)

    def __getattribute__(self, word):
      if word in super().__getattribute__('_words'):
            return super().__getattribute__('_words')[word]
      else:
            return super().__getattribute__(word)

# - new_word (word, value) - creating a new word in the dictionary. (called in __setattr__, __setitem__ )
# If value is an object of the Word class, then check if word and
# _word (throw ValueError in case of mismatch).
# If value is a string, create a Word object,
# using value as one of the translations.

    def new_word (self, word, value):
        if isinstance(value, str):
            new = Word(word,value)
            self._words[new._word] = new
        elif isinstance(value, Word):
            if word == value._word:
                self._words[value._word] = value
            else:
              raise ValueError(f'Key {word} is not the same with {value._word}')
        else:
            raise TypeError (f'Error type, expected to be str or Word, found {type(value)}')


#- __setattr__ adds a word to the dictionary (implementation conditions in new_word)
    def __setattr__(self, word1, value1):
        self.new_word(word1,value1)


#- __delattr__, delite word from dictionary
    def __delattr__(self, word):
        self._words.pop(word)


#- __getitem__(word),  returning a Word object by the word key from _words
    def __getitem__(self, word):
        if word in self._words:
            return super().__getattribute__('_words')[word]
        else:
            raise KeyError(f"Key {word} don't found")


#- __setitem__(word, value) - creating a new word in the dictionary (implementation conditions in new_word)
    def __setitem__(self, word1, value1):
        self.new_word(word1, value1)


#- __len__ -  returning the number of words in the dictionary
    def __len__(self):
        i = 0
        for key in self._words:
            i = i+1
        return i


#- __str__ - returning a string like “EN-UA Vocabulary (<number> words)”.
    def __str__(self):
        return f"EN-UA Vocabulary ({len(self)} words)"


#___________________________________________________________
v1 = Vocabulary()
v1+w1
v1+w3
w4 = Word('pound','пруд')

print('\nCreate a dictionary and add 2 words to the dictionary via +')
print(v1._words)

print('\nFind the number of words in the dictionary')
print(len(v1))

print('\nRemove the word water from the dictionary and see whats left.')
del (v1.water)
print(v1._words)

v1+w4

print('\nThrough __getitem__ [rain] return the word-translation object')
print(v1['rain'])


print('\nAdd a new word via __setattr__ and __setitem__, check if value is an object and string')
w5 = Word('father','папа')
v1.new_word('father',w5)
v1.new_word('mother','мама')
print(v1._words)

v1.work = 'рaбота'
print(v1._words)

v1['window'] = 'вікно'
print(v1._words)

print('\Call __str__ ')
print(v1)

print('\Call __getattribute__ ')
print(v1.rain)