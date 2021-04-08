from requests import get
from bs4 import BeautifulSoup
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import urllib.request

def process_age(actors):
    group_30 = []
    group_60 = []
    group_100 = []
    for i in range(0,10):
        img1=cv2.imread(str("img_"+str(i)+".jpg"))
        plt.imshow(img1[:,:,::-1])
        plt.show()
        result = DeepFace.analyze(img1,actions=['age'])
        actor_age = str(actors[i])+": "+str(result['age'])
        if result['age'] > 0 and result['age'] < 31:
            group_30.append(actor_age)
        elif result['age'] > 30 and result['age'] < 61:
            group_60.append(actor_age)
        else:
            group_100.append(actor_age)
    print()
    print("########################")
    print("### AGE GROUP 0-30 ###")
    print(group_30)
    print()
    print("### AGE GROUP 31-60 ###")
    print(group_60)
    print()
    print("### AGE GROUP 61-100 ###")
    print(group_100)
    print("########################")
    print()

def process_race(actors):
    group_asian = []
    group_indian = []
    group_black = []
    group_white = []
    group_middleeast = []
    group_latino = []
    group_hispanic = []
    for i in range(0,10):
        img1=cv2.imread(str("img_"+str(i)+".jpg"))
        plt.imshow(img1[:,:,::-1])
        plt.show()
        result = DeepFace.analyze(img1,actions=['race'])
        race = result['race']
        max_per = max(race, key=race.get)
        actor_race = str(actors[i])+": "+str(max_per)
        if max_per == "asian":
            group_asian.append(actor_race)
        elif max_per == "indian":
            group_indian.append(actor_race)
        elif max_per == "black":
            group_black.append(actor_race)
        elif max_per == "white":
            group_white.append(actor_race)
        elif max_per == "middle eastern":
            group_middleeast.append(actor_race)
        elif max_per == "latino":
            group_latino.append(actor_race)
        elif max_per == "hispanic":
            group_hispanic.append(actor_race)
    print()
    print("########################")
    print("### Race GROUP Asian ###")
    print(group_asian)
    print()
    print("### Race GROUP Indian ###")
    print(group_indian)
    print()
    print("### Race GROUP Black ###")
    print(group_black)
    print()
    print("### Race GROUP white ###")
    print(group_white)
    print()
    print("### Race GROUP middle east ###")
    print(group_middleeast)
    print()
    print("### Race GROUP latino ###")
    print(group_latino)
    print()
    print("### Race GROUP hispanic ###")
    print(group_hispanic)
    print("########################")
    print()

def process_emotion(actors):
    group_angry = []
    group_disgust = []
    group_fear = []
    group_happy = []
    group_sad = []
    group_surprise = []
    group_neutral = []
    for i in range(0,10):
        img1=cv2.imread(str("img_"+str(i)+".jpg"))
        plt.imshow(img1[:,:,::-1])
        plt.show()
        result = DeepFace.analyze(img1,actions=['emotion'])
        emotion = result['emotion']
        max_per = max(emotion, key=emotion.get)
        actor_emotion = str(actors[i])+": "+str(max_per)
        if max_per == "angry":
            group_angry.append(actor_emotion)
        elif max_per == "disgust":
            group_disgust.append(actor_emotion)
        elif max_per == "fear":
            group_fear.append(actor_emotion)
        elif max_per == "happy":
            group_happy.append(actor_emotion)
        elif max_per == "sad":
            group_sad.append(actor_emotion)
        elif max_per == "surprise":
            group_surprise.append(actor_emotion)
        elif max_per == "neutral":
            group_neutral.append(actor_emotion)
    print()
    print("########################")
    print("### Emotion GROUP angry ###")
    print(group_angry)
    print()    
    print("### Emotion GROUP Disgust ###")
    print(group_disgust)
    print()
    print("### Emotion GROUP fear ###")
    print(group_fear)
    print()    
    print("### Emotion GROUP happy ###")
    print(group_happy)
    print()
    print("### Emotion GROUP sad ###")
    print(group_sad)
    print()
    print("### Emotion GROUP surprise ###")
    print(group_surprise)
    print()
    print("### Emotion GROUP neutral ###")
    print(group_neutral)
    print("########################")
    print()

def process_gender(actors):
    group_male = []
    group_female = []
    for i in range(0,10):
        img1=cv2.imread(str("img_"+str(i)+".jpg"))
        plt.imshow(img1[:,:,::-1])
        plt.show()
        result = DeepFace.analyze(img1,actions=['gender'])
        actor_gender = str(actors[i])+": "+str(result['gender'])
        if result['gender'] == "Man":
            group_male.append(actor_gender)
        else:
            group_female.append(actor_gender)
    print()
    print("########################")
    print("### Gender GROUP MALE ###")
    print(group_male)
    print()
    print("### Gender GROUP Female ###")
    print(group_female)
    print()
    print("########################")
    print()



print(
'''

Name    : Divyansh Rahangdale
Roll    : 18100BTCSES02782
Subject : Data Science 

''')
print()
actors = ["img_1.jpg","img_2.jpg","img_3.jpg","img_4.jpg","img_5.jpg","img_6.jpg","img_7.jpg","img_8.jpg","img_9.jpg","img_10.jpg",]
img_url = ""
actors_name = []
count = 0
url = 'https://www.imdb.com/list/ls050745379/'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
actors = html_soup.find_all('div', class_='lister-list')
select_img = actors[0].findAll('div', class_='lister-item-image')
for img in select_img: 
    img_tag = img.find('img')
    actor_name = img_tag.get('alt')
    img_url = img_tag.get('src')
    img_name = str("img_"+str(count)+".jpg")
    actors_name.append(str(actor_name))
    r = urllib.request.urlopen(img_url)
    with open(img_name, "wb") as f:
        f.write(r.read())
    count = count+1
    if count == 10:
        break

process_age(list(actors_name))
process_race(list(actors_name))
process_emotion(list(actors_name))
process_gender(list(actors_name))
