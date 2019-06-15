# -*- coding: utf-8 -

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import os
from tqdm import tqdm
from random import shuffle
import cv2


from google.colab import drive
drive.mount("/content/drive")
train_file="/content/drive/My Drive/Colab Notebooks/train.zip"
test_file="/content/drive/My Drive/Colab Notebooks/test.zip"



import zipfile
with zipfile.ZipFile(train_file,'r') as z:
  z.extractall()
with zipfile.ZipFile(test_file,'r') as z:
  z.extractall()

  
TEST_DIR="./test/"
TRAIN_DIR="./train/"
LEARNING_RATE=1e-3
MODEL_NAME="dogsvscats-{}-{}".format(LEARNING_RATE,'CNN')
IMG_SIZE=50




def label_image(img):
  img_name=img.split('.')[-3]
  if img_name=='cat':
     return [1,0]
  elif img_name=='dog':
     return [0,1] 
def create_train_data():
  training_data=[]
  for img in tqdm(os.listdir(TRAIN_DIR)):
    label=label_image(img)
    path=os.path.join(TRAIN_DIR,img)
    img=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    img=cv2.resize(img,(IMG_SIZE,IMG_SIZE))
    training_data.append([np.array(img),np.array(label)])
  shuffle(training_data)
  np.save('train_data.npy',training_data)
  return training_data

    
train_data=create_train_data()    


import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression




convet = input_data(shape=[None,IMG_SIZE,IMG_SIZE,1], name='input')
convet = conv_2d(convet,32,5,activation='relu')
convet = max_pool_2d(convet,5)
convet = conv_2d(convet,64,5,activation='relu')
convet = max_pool_2d(convet,5)
convet = fully_connected(convet,2,activation='relu')
convet = dropout(convet,0.8)
convet = fully_connected(convet,2,activation='softmax')
convet = regression(convet,optimizer='adam',learning_rate=LEARNING_RATE,loss='categorical_crossentropy', name='targets')
model = tflearn.DNN(convet,tensorboard_dir='log')


if os.path.exists('{}.meta'.format(MODEL_NAME)):
  model.load(MODEL_NAME)
  print('model loaded')
  
train = train_data[:-500]
test = train_data[-500:]


X = np.array([i[0] for i in train]).reshape(-1,IMG_SIZE,IMG_SIZE,1)
Y = [i[1] for i in train]

test_x=np.array([i[0] for i in test]).reshape(-1,IMG_SIZE,IMG_SIZE,1)
test_y=[i[1] for i in test]

 model.fit({'input': X}, {'targets': Y}, n_epoch=5, validation_set=({'input': test_x}, {'targets': test_y}), 
        snapshot_step=500, show_metric=True, run_id=MODEL_NAME)