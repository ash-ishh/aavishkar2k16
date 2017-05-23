import cv2
import os
import string
import random

name = input("Enter name..\n")

os.chdir("dataset/")
if not os.path.exists(name):
    os.mkdir(name)
os.chdir(name)

fc = cv2.CascadeClassifier('/home/ash-ishh/Aavishkar/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
randomalpha = list(string.ascii_lowercase)


count = 10
_,im = cam.read()

while count < 150:
    _,im = cam.read()
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = fc.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        if (count%10 == 0):
            name = randomalpha[random.randint(0,len(randomalpha)-1)] 
            face = gray[y:y+h,x:x+w]
            face_resize = cv2.resize(face,(100,100))
            cv2.imwrite("{}{}.jpg".format(name,count),face_resize)
    count += 1

    cv2.imshow("tmp",im)
    key = cv2.waitKey(10)
    if key == 27:
        break
