# -*- coding: utf-8 -*-
"""MultipleLR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LPX9IwwnHObObiLlXxImXDrIe8kmUoUH
"""

from google.colab import drive
drive.mount('/content/drive')

"""## Importing Libraries"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

"""## Loading the dataset"""

data = pd.read_csv("/content/drive/MyDrive/Real estate.csv")

data

"""## Inputs and Labels"""

X = data.iloc[:,1:7].values
Y = data.iloc[:,7].values

X

Y

"""## Handling missing values if any """

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy = 'mean')
imputer.fit(X)
X = imputer.transform(X)

X.shape

"""## Train Test split """

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state = 50)

X_test.shape

from sklearn.preprocessing import Normalizer
sc = Normalizer()
X_train = sc.fit_transform(X_train)
X_test = sc.transform (X_test)

X_train

"""## Fitting the model"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

"""## Predicting on the test set """

Y_pred = regressor.predict(X_test)
np.set_printoptions(precision = 1)
print(np.concatenate((Y_pred.reshape(len(Y_pred),1),Y_test.reshape(len(Y_test),1)),1))

from sklearn.metrics import r2_score
print(r2_score(Y_test,Y_pred))

from sklearn.metrics import r2_score
print(r2_score(Y_train,regressor.predict(X_train)))

from sklearn import metrics
MAE= metrics.mean_absolute_error(Y_test, Y_pred)
MSE= metrics.mean_squared_error(Y_test, Y_pred)
RMSE= np.sqrt(MSE)

MAE

MSE

RMSE

sns.scatterplot(x=Y_test, y=Y_pred, color='#20d489')
plt.axhline(y=30, color='#105c3c', ls='--')

