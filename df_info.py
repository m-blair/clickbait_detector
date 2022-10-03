import collections

import pandas as pd
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import contractions
import re
from matplotlib import cm

stop_words = set(stopwords.words('english'))


def split_data(df: pd.DataFrame, col_title=''):
    """
    Splits a dataframe with boolean column 'label' into two, by value. \n
    :param col_title: title of column with binary values to split by
    :param df: a dataframe with boolean column 'label'
    :return: two dataframes containing only entries with value of 0's and 1's, respectively
    """
    df1 = df[df[col_title] == 0]
    df2 = df[df[col_title] == 1]
    return df1, df2


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


def counter_to_df(counter: collections.Counter, n: int = 10):
    df = pd.DataFrame.from_dict(counter, orient='index').reset_index(inplace=False)
    df = df.sort_values(by=[0], ascending=False)[:n]
    df = df.rename(columns={'level_0': 'old index'})
    df = df.reset_index(inplace=False)
    return df


#%%
