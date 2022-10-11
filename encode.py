import collections
import numpy as np
import pandas as pd
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import contractions
import re
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
import preprocessor


def vectorize(df: pd.DataFrame):
    """
    :param df: single column dataframe of string text
    :return: document-term matrix and a vocabulary
    """
    vectorizer = CountVectorizer(max_features=20000)
    vectorized = vectorizer.fit_transform(df)
    vocab = vectorizer.get_feature_names()
    return vectorized.toarray(), vocab


def to_doc_term_matrix(str_from_user: str, train_data: pd.DataFrame):
    """
    Transforms a user input string to a document-term matrix, fitted on the provided data \n
    :param str_from_user: an article headline as a string
    :param train_data: dataframe of training data
    :return: a sparse document-term matrix created from str_from_user
    """

    vectorizer = CountVectorizer()
    df = pd.DataFrame([str_from_user], columns=['headline'])
    cleaned = preprocessor.clean_data(df)
    vectorizer.fit(train_data)
    transformed = vectorizer.transform(cleaned).toarray()
    return transformed







