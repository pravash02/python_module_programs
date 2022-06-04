
''' PyDictionary '''
from PyDictionary import PyDictionary
word = "aaaaa"
dictionary = PyDictionary(word)
res = PyDictionary(word).getMeanings()
if res[word] == None:
    print('word not found')
else:
    print('word found')


###############################

''' nltk '''
from nltk.corpus import words as nltk_words
def is_english_word(word):
    # creation of this dictionary would be done outside of
    #     the function because you only need to do it once.
    dictionary = dict.fromkeys(nltk_words.words(), None)
    try:
        x = dictionary[word]
        return True
    except KeyError:
        return False
is_english_word('hel')


###############################

''' pyenchant '''

# import enchant
# e = enchant.Dict("en_US")
