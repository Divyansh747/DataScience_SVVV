from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

actors = ['actor.jpeg', 'actor1.jpg', 'actor2.jpg', 'actor3.jpg']
for path in actors:
    img1=cv2.imread("/root/SVVV_6SEM/DataScience/practical/Deepface/" + path)
    plt.imshow(img1[:,:,::-1])
    plt.show()
    result = DeepFace.analyze(img1,actions=['gender'])
    print("Predicted age of actor is :",result['gender'])
