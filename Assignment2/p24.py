from nltk.corpus import stopwords
import nltk
from bs4 import BeautifulSoup
import urllib.request

response = urllib.request.urlopen('https://docs.python.org/3/whatsnew/3.9.html')

html = response.read()

soup = BeautifulSoup(html,"html5lib")

text = soup.get_text(strip=True)

tokens = [t for t in text.split()]

nltk.download('stopwords')
stopwords.words('english')
clean_tokens = tokens[:]

sr = stopwords.words('english')

for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

for key,val in freq.items():
    print (str(key) + ':' + str(val))
freq.plot(20,cumulative=False)


