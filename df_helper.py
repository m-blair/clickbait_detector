# auxiliary methods for manipulating dataframe content
import collections

import pandas as pd
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import contractions
import re

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


def counter_to_df(counter: collections.Counter, n: int = 10):
    df = pd.DataFrame.from_dict(counter, orient='index').reset_index(inplace=False)
    df = df.sort_values(by=[0], ascending=False)[:n]
    df = df.rename(columns={'level_0': 'old index'})
    df = df.reset_index(inplace=False)
    return df
