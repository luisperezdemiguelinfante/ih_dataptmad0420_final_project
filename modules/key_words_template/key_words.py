import xlrd
import os

from nltk.corpus import stopwords
from openpyxl import Workbook, drawing
import openpyxl
import warnings
import spacy
import pandas as pd
import string

from spacy import tokenizer
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import es_core_news_sm
import nltk
from nltk.tokenize import RegexpTokenizer


file = ("//Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/raw/garnica.xlsx")
data = pd.ExcelFile(file)

df = data.parse('dedicaciones')
df['task description']= df['task description'].astype(str)

def key_words_column(template):
    def remove_stopwords(text):
        words = [w for w in text if w not in stopwords.words('spanish')]

        return words

    df['key_words'] = df['task description'].apply(lambda x: remove_stopwords(x))

    def remove_punctuation(text):
        no_punct = "".join([c for c in text if c not in string.punctuation])


        return no_punct

    tokenizer = RegexpTokenizer(r'\w+')
    df['no_punt'] = df['task description'].apply(lambda x: remove_punctuation(x))
    df['token'] = df['no_punt'].apply(lambda x: tokenizer.tokenize(x.lower()))
    df['key_words'] = df['token'].apply(lambda x: remove_stopwords(x))
    key_words_template=df.drop(['no_punt', 'token'], axis='columns', inplace=True)
    key_words_template = df

    with pd.ExcelWriter('key_words_template.xlsx') as writer:
        key_words_template.to_excel(writer, sheet_name='key_words_template')


    return key_words_template

