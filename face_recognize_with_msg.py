import cv2, sys, numpy
import os
import pickle
import datetime
import sendmessage

def end():
    exit(0)

size = 4
haar_file = '/home/ash-ishh/Aavishkar/haarcascade_frontalface_default.xml'
now = datetime.datetime.now()

images = pickle.load(open("images.p","rb"))
labels = pickle.load(open("labels.p","rb"))
names = pickle.load(open("names.p","rb"))
targets = open("target.txt","r").readlines()
targets = [target.strip('\n') for target in targets]
suspect_no = 0

os.chdir("logs")
os.mkdir(str(now))
os.chdir(str(now))

model = cv2.face.createFisherFaceRecognizer()
model.train(images, labels)

face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)

while True:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (100,100))
        prediction = model.predict(face_resize)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
        if prediction[1]<500:

             cv2.putText(im,'%s - %.0f' % (names[prediction[0]],prediction[1]),(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
             if not os.path.isfile(names[prediction[0]]+".txt"):
                 facefile = open((names[prediction[0]])+".txt","w")

             facefile = open((names[prediction[0]])+".txt","a")
             facefile.write(str(datetime.datetime.now())+"\n")

             if names[prediction[0]] in targets:
                 print("Suspect found!")
                 sendmessage.send(names[prediction[0]]+ " spotted at " + str(datetime.datetime.now()) )              
                 print("Message Sent!")
                 end()
        else:
    	    cv2.putText(im,'not recognized',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))

    cv2.imshow('Output', im)
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        facefile.close()
