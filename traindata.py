import pickle
import os
import cv2
import numpy

datasets = '/home/ash-ishh/Aavishkar/dataset/' 

print("Training..")
 
(images, labels, names, id) = ([], [], {}, 0) 
for (subdirs, dirs, files) in os.walk(datasets): 
    for subdir in dirs: 
        names[id] = subdir 
        subjectpath = os.path.join(datasets, subdir) 
        for filename in os.listdir(subjectpath): 
            path = subjectpath + '/' + filename 
            label = id 
            images.append(cv2.imread(path, 0)) 
            labels.append(int(label)) 
        id += 1 
(width, height) = (130, 100) 
 
(images, labels) = [numpy.array(lis) for lis in [images, labels]] 

pickle.dump(images,open("images.p","wb"))
pickle.dump(labels,open("labels.p","wb"))
pickle.dump(names,open("names.p","wb"))

print("Done..")
