import nltk
import pandas as pd
import numpy as np
import re
import string
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import pos_tag
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


print(
'''

Name      : Divyansh Rahangdale
Roll no   : 18100BTCSES02782
Class     : Data Science LAB
Aim       : Write a programme in Python to perform sentiment analysis for Movie Review

'''
)
#nltk.download('averaged_perceptron_tagger')
#nltk.download('word')
#nltk.download('wordnet')

# Read CSV File
data = pd.read_csv('IMDB_SENTIMENT1.csv')

def remove_features(data_str):
    url_re = re.compile('https?://(www.)?\w+\.\w+(/\w+)*/?') 
    punc_re = re.compile('[%s]' % re.escape(string.punctuation)) 
    num_re = re.compile('(\\d+)')
    mention_re = re.compile('@(\w+)')
    alpha_num_re = re.compile("^[a-z0-9_.]+$")
    # convert to lowercase
    data_str = data_str.lower()
    # remove hyperlinks
    data_str = url_re.sub(' ', data_str)
    # remove @mentions
    data_str = mention_re.sub(' ', data_str)
    # remove puncuation
    data_str = punc_re.sub(' ', data_str)
    # remove numeric 'words'
    data_str = num_re.sub(' ', data_str)
    # remove non a-z 0-9 characters and words shorter than 1 characters 
    list_pos = 0
    cleaned_str = ''
    for word in data_str.split():
        if list_pos == 0:
            if alpha_num_re.match(word) and len(word) > 1:
                cleaned_str = word 
            else:
                cleaned_str = ' '
        else:
            if alpha_num_re.match(word) and len(word) > 1:
                cleaned_str = cleaned_str + ' ' + word 
            else:
                cleaned_str += ' '
        list_pos += 1
    
    return " ".join(cleaned_str.split())

data_clean = []
for i in range(len(data)):
    res = remove_features(data['review'][i])
    data_clean.append(res)

reviews = pd.DataFrame()
reviews[1] = data_clean
reviews[2] = data['sentiment']
reviews.columns = ['review','sentiment']

#train dataset
X_train=reviews.review[:1000]
Y_train=reviews.sentiment[:1000]
#test dataset
X_test=reviews.review[1000:]
Y_test=reviews.sentiment[1000:]

cv = CountVectorizer(stop_words='english')
X_train_cv = cv.fit_transform(X_train)
X_test_cv = cv.transform(X_test)

X_train_cv = pd.DataFrame(X_train_cv.toarray(), columns=cv.get_feature_names())
X_test_cv = pd.DataFrame(X_test_cv.toarray(), columns=cv.get_feature_names())

# Use a logistic regression model
lr = LogisticRegression()
lr.fit(X_train_cv, Y_train)
y_pred_cv = lr.predict(X_test_cv)
print("Accuracy of LogisticRegression: {}".format(accuracy_score(Y_test, y_pred_cv)))

# sample data 1
sample_data = "worst movie, because of false logic !"
clean_data = remove_features(sample_data)

X_sample_test = cv.transform([clean_data])
X_sample_test = pd.DataFrame(X_sample_test.toarray(), columns=cv.get_feature_names())

y_pred_cv = lr.predict(X_sample_test)
print(y_pred_cv)

# sample data 2
sample_data = "good movie, also acting of actors is amazing !"
clean_data = remove_features(sample_data)

X_sample_test = cv.transform([clean_data])
X_sample_test = pd.DataFrame(X_sample_test.toarray(), columns=cv.get_feature_names())

y_pred_cv = lr.predict(X_sample_test)
print(y_pred_cv)
