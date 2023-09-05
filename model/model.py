#importing libraries
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

#loading the data file
data_dict=pickle.load(open('D:/my python/python code/final_submission/model/data.pickle','rb'))
data=np.asarray(data_dict['data'])
labels=np.asarray(data_dict['labels'])

#splitting the data set into train and test 
x_train,x_test,y_train,y_test=train_test_split(data,labels,test_size=0.2,shuffle=True,
                                               stratify=labels)
#initiallizing the classifier
classifier=RandomForestClassifier()
classifier.fit(x_train,y_train)

#predictiing to check accuracy
y_predict=classifier.predict(x_test)

#checking accuracy 
score=accuracy_score(y_predict,y_test)
print('{}% of samples were classified correctly !'.format(score * 100))

#Saving the model for further use
f = open('D:/my python/python code/final_submission/model/classifier.p', 'wb')
pickle.dump({'classifier': classifier}, f)
f.close()