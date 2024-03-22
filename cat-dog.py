import numpy as np
import pandas as pd
from tensorflow import keras
from keras.layers import Conv2D, MaxPooling2D,Dense,Flatten
from keras.models import Sequential

X_train = np.loadtxt('input.csv',delimiter=',')
Y_train = np.loadtxt('labels.csv',delimiter=',')

X_test = np.loadtxt('input_test.csv',delimiter=',')
Y_test = np.loadtxt('labels_test.csv',delimiter=',')

print("shape of X_train: ",X_train.shape)
print("shape of Y_train: ",Y_train.shape)
print("shape of X_test: ",X_test.shape)
print("shape of Y_test: ",Y_test.shape)