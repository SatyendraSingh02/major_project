#importing the required libraries
import os
import cv2

#initializing the directory 
DATA_DIR = 'D:/my python/python code/new/data/'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

#initalizing the required varibles
number_of_classes = 36  #no of classes
dataset_size = 100      #no of samples for each class

#initializing the OpenCv webcam option 
cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))
    done = False
while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "R" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break
counter = 0
while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)
        counter += 1
        
#realesing the web cam 
cap.release()
cv2.destroyAllWindows()