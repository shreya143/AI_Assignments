#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow as tf
from tensorflow  import keras


# In[21]:


import numpy as np
import matplotlib.pyplot as plt


# In[22]:


print(tf._version_)


# In[23]:


fashion_mnist = keras.datasets.fashion_mnist


# In[24]:


(train_images,train_labels),(test_images,test_labels)=fashion_mnist.load_data()


# In[25]:


class_names = {'T-shirt/top','Trouser','pullover','dress','coat','sandal','Shirt','sneaker','Bag','Ankle boot'}


# In[26]:


train_images.shape


# In[27]:


len(train_labels)


# In[ ]:


train_labels


# In[ ]:


test_images.shape


# In[ ]:


len(test_labels)


# In[ ]:


plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()


# In[ ]:


train_images = train_images/255.0
test_images = test_images/255.0


# In[30]:


plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i],cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()    
    
    
    

