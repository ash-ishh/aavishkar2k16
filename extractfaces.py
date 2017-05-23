import cv2
import os
import sys

os.chdir('/home/ash-ishh/Aavishkar/InstaCrawl/')
usr = sys.argv[1]
os.chdir(usr)
imgs = [each for each in os.listdir()]

if not os.path.exists("/home/ash-ishh/Aavishkar/dataset/"+usr):
	os.mkdir("/home/ash-ishh/Aavishkar/dataset/"+usr)


fc = cv2.CascadeClassifier('/home/ash-ishh/Aavishkar/haarcascade_frontalface_default.xml')

for each in imgs:
	img = cv2.imread(each)
	try:
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	except:
		pass

	faces = fc.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30,30),
			flags=cv2.CASCADE_SCALE_IMAGE
			)
	if type(faces) == tuple: #if no face found
		pass
	else:
		try:
			for (x,y,w,h) in faces:
				face = gray[y:y+h,x:x+w]
				face_norm = cv2.equalizeHist(face)
				face_norm = cv2.resize(face_norm,(100,100))
				cv2.imwrite(os.path.join("/home/ash-ishh/Aavishkar/dataset/"+usr,each),face_norm)
			print(each+" done!")
		except Exception as e:
			print(str(e))
