import collections
import sys
import nltk

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

import Text_Wash


def Word_Count(text):
    new_text = Text_Wash.Wash(text)
    En_stopwords = stopwords.words("english")
    words = new_text.split()
    new_words = []

    if words:
        tags = nltk.pos_tag(words)

    for tag in tags:
        word = tag[0]
        kind = Word_Kind(tag[1])
        if kind:
            lemmatized_word = WordNetLemmatizer().lemmatize(word, kind)
            new_words.append(lemmatized_word)
        else:
            new_words.append(word)

    Final_Text = []
    for word in new_words:
        if word not in En_stopwords:
            Final_Text.append(word)

    Word_frenquency = collections.Counter(Final_Text)
    return Word_frenquency


def Word_Kind(wordkind):
    if wordkind.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif wordkind.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif wordkind.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    elif wordkind.startswith('R'):
        return nltk.corpus.wordnet.ADV
    else:
        return ''
