import collections

import pandas as pd
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import contractions
import re

stop_words = set(stopwords.words('english'))


def remove_stopwords(line):
    tokenwords = nltk.word_tokenize(line)
    result = [word for word in tokenwords if word not in stop_words]
    result = []
    for word in tokenwords:
        if word not in stop_words:
            result.append(word)
    return ' '.join(result)


def clean_data(df: pd.DataFrame, remove_sw=True):
    lowercase = df.headline.apply(lambda x: str(x).lower())
    # expand contractions
    expanded = lowercase.apply(lambda x: contractions.fix(x, slang=False))
    # remove punct (keep periods and hyphens)
    no_punct = expanded.apply(lambda x: re.sub(r"[^a-zA-Z0-9\-\.]", " ", x))
    # remove single characters
    fixed = no_punct.apply(lambda x: ' '.join([w for w in x.split() if len(w) > 1]))
    # clean up any excess spacing left over from previous steps
    cleaned = fixed.apply(lambda x: re.sub(' +', ' ', x))
    if remove_sw:
        cleaned = cleaned.apply(lambda x: remove_stopwords(x))
    return cleaned
