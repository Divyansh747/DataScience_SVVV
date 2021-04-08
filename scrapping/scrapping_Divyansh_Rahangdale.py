'''
Name      : Divyansh Rahangdale
Roll no   : 18100BTCSES02782
Class     : Data Science LAB
Aim       : Write a python program to scrap data
Scrap url : https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia
'''

from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia"
pg = requests.get(url).text
sp = BeautifulSoup(pg,"lxml")
sections = sp.find_all(class_='flex-row')

A=[]
B=[]
C=[]

for section in sections:
    title = section.find('h2', class_='title')
    company = section.find('div', class_='company')
    location = section.find('div', class_='location')
    if title==None and company==None and location==None:
        continue
    A.append(title.text.strip())
    B.append(company.text.strip())
    C.append(location.text.strip())

df = pd.DataFrame()
df["Title"]=A
df["Company"]=B
df["location"]=C
print(df)
