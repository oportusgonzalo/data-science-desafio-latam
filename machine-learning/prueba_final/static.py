
import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt
import time
import seaborn as sns
import string
import os

import re
import nltk.corpus

nltk.download('punkt')
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
from nltk.corpus import stopwords


stop_words = stopwords.words('english')

def clean_text(df, col_name, new_col_name):
    # column values to lower case
    df[new_col_name] = df[col_name].str.lower().str.strip()
    # removes special characters
    df[new_col_name] = df[new_col_name].apply(lambda x: re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z.% \t])", "", x))
    return df

def replace_stop_words(df, col, stop_list):
    df['{}_stop'.format(col)] = df[col].apply(lambda x: ' '.join([word for word in x.split() if x not in stop_list]))
    return df

def word_lemmatizer(text):
    text_lemma = [WordNetLemmatizer().lemmatize(word) for word in text]
    return text_lemma

def nlp_cleaning(df):
    # normalization
    df = clean_text(df, 'content', 'content_norm')
    # remove stop words
    df = replace_stop_words(df, 'content_norm', stop_words)
    # removing numbers
    df['content_norm_stop'] = df['content_norm_stop'].apply(lambda x: re.sub('[0-9]+', '', x))
    # tokenize text
    df['content_token'] = df['content_norm_stop'].apply(lambda x: word_tokenize(x))
    # lemmatization
    df['content_token_lemma'] = df['content_token'].apply(lambda x: word_lemmatizer(x))
    # joining lemmas and removing punctuation
    df['content_clean'] = df['content_token_lemma'].apply(lambda list_: ' '.join([word for word in list_ if word not in string.punctuation]))
    return df

#calidad de datos
def calidad_datos(data):
    tipos = pd.DataFrame({'tipo': data.dtypes},index=data.columns)
    na = pd.DataFrame({'nulos': data.isna().sum()}, index=data.columns)
    na_prop = pd.DataFrame({'porc_nulos':data.isna().sum()/data.shape[0]}, index=data.columns)
    ceros = pd.DataFrame({'ceros':[data.loc[data[col]==0,col].shape[0] for col in data.columns]}, index= data.columns)
    ceros_prop = pd.DataFrame({'porc_ceros':[data.loc[data[col]==0,col].shape[0]/data.shape[0] for col in data.columns]}, index= data.columns)
    summary = data.describe(include='all').T

    summary['dist_IQR'] = summary['75%'] - summary['25%']
    summary['limit_inf'] = summary['25%'] - summary['dist_IQR']*1.5
    summary['limit_sup'] = summary['75%'] + summary['dist_IQR']*1.5

    summary['outliers'] = data.apply(lambda x: sum(np.where((x<summary['limit_inf'][x.name]) | (x>summary['limit_sup'][x.name]),1 ,0)) if x.name in summary['limit_inf'].dropna().index else 0)


    return pd.concat([tipos, na, na_prop, ceros, ceros_prop, summary], axis=1).sort_values('tipo')