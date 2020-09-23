#!/usr/bin/env python
# coding: utf-8

# In[90]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import colors
# from PIL import Image
import pandas as pd
import collections
from linecache import getline

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import seaborn as sn
plt.style.use('ggplot')
import math

# get_ipython().magic(u'matplotlib inline')
matplotlib.rcParams['figure.figsize'] = (20,10)


# In[ ]:





# In[19]:

#
# img = plt.imread('Floods/testdata/awe43d11feb16/AW-NE43D-099-059A-11Feb16-BAND2.tif')
# plt.imshow(img[:], cmap=plt.cm.coolwarm)
# img = plt.imread('Floods/testdata/awe43d11feb16/AW-NE43D-099-059A-11Feb16-BAND3.tif')
# plt.imshow(img[:], cmap=plt.cm.coolwarm)
# img = plt.imread('Floods/testdata/awe43d11feb16/AW-NE43D-099-059A-11Feb16-BAND4.tif')
# plt.imshow(img[:], cmap=plt.cm.coolwarm)
# img = plt.imread('Floods/testdata/awe43d11feb16/AW-NE43D-099-059A-11Feb16-BAND5.tif')
# plt.imshow(img[:], cmap=plt.cm.coolwarm)
#




# In[49]:


np.random.seed(10)


# In[50]:


# Venice Water Level Dataset from 1983 to 2015
dataframe = pd.read_csv('./venezia.csv', usecols=[1], engine='python', skipfooter=3)
dataset   = dataframe.values
dataset   = dataset.astype('float32')
dataframe.head()


# In[76]:


plt.plot(dataset)


# In[53]:


water_levels = dataframe['level'].values.tolist()


# In[54]:


cleaned_levels = []
                 
for i in water_levels:
    if i >= 0:
        cleaned_levels.append(i)


# In[59]:


df_clean = pd.DataFrame(cleaned_levels)


# In[77]:


plt.plot(df_clean)


# In[65]:


# normalize the dataset
scaler  = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)


# In[96]:


# split into train and test sets

percentage_train = 0.80

train_size  = int(len(dataset) * percentage_train)
test_size   = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
print("Training Datapoints :", len(train), "testing Datapoints :", len(test))


# In[97]:


print('--- Training Data ---', percentage_train * 100, '% ---')
plt.plot(train)
plt.show()
print('--- Test Data ---', 100-(percentage_train * 100), '% ---')
plt.plot(test)
plt.show()


# In[98]:


# This function creates a sliding window of the dataset.
# applying a window or batch of dataset make batched features dataset
# converting a problem in a nested loop, to reduce the time complexity.


"""
LSTMs do not require a sliding window of inputs. They can remember what they have seen in the past, and if you feed in training examples one at a time they will choose the right size window of inputs to remember on their own.

LSTM's are already prone to overfitting, and if you feed in lots of redundant data with a sliding window then yes, they are likely to overfit.
On the other hand, a sliding window is necessary for time series forecasting with Feedforward Neural Networks, because FNNs require a fixed size input and do not have memory, so this is the most natural way to feed them time series data.
Whether or not the FNN will overfit depends on its architecture and your data, but all standard regularization techniques will apply if it does. For example you can try choosing a smaller network, L2 regularization, Dropout, etc.
"""
# in simple words cutting down the data into chunks of data.
def create_dataset(dataset, sliding_window=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-sliding_window-1):
        a = dataset[i:(i+sliding_window), 0]
        dataX.append(a)
        dataY.append(dataset[i + sliding_window, 0])
    return np.array(dataX), np.array(dataY)


# In[99]:


# use a n-1 sliding window equivalent to 1 hours of historical data -10
slide_window   = 1
trainX, trainY = create_dataset(train, slide_window)
testX, testY   = create_dataset(test, slide_window)


# In[100]:


trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX  = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))


# In[ ]:


#Setup the LSTM

model = Sequential()
model.add(LSTM(4, input_dim=slide_window))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, nb_epoch=50, batch_size=1, verbose=2)


# In[ ]:


# Print out the evaluation for both the
trainScore = model.evaluate(trainX, trainY, verbose=0)
trainScore = math.sqrt(trainScore)
trainScore = scaler.inverse_transform(np.array([[trainScore]]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = model.evaluate(testX, testY, verbose=0)
testScore = math.sqrt(testScore)
testScore = scaler.inverse_transform(np.array([[testScore]]))
print('Test Score: %.2f RMSE' % (testScore))


# In[ ]:




