
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
    # tokenize text
    df['content_token'] = df['content_norm_stop'].apply(lambda x: word_tokenize(x))
    # lemmatization
    df['content_token_lemma'] = df['content_token'].apply(lambda x: word_lemmatizer(x))
    # joining lemmas
    df['content_clean'] = df['content_token_lemma'].apply(lambda list_: ' '.join([word for word in list_]))
    return df