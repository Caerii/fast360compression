#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
Linear Regression Example
=========================================================
The example below uses only the first feature of the `diabetes` dataset,
in order to illustrate the data points within the two-dimensional plot.
The straight line can be seen in the plot, showing how linear regression
attempts to draw a straight line that will best minimize the
residual sum of squares between the observed responses in the dataset,
and the responses predicted by the linear approximation.

The coefficients, residual sum of squares and the coefficient of
determination are also calculated.
"""
print(__doc__)


# Code source: Jaques Grobler
# License: BSD 3 clause


import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Load the dataset for saliency scores
# each macroblock should count as one input (a row vector), and the output is the saliency score
# we want to split the dataset into training and testing sets
# We will be doing prediction for 450 lines in the DCT_With_SaliencyWrite.txt file
# This counts for 10 frames in the video, we will assume 80(columns)x45(rows)x10(frames) = 36000
dataset = pd.read_csv('/home/alif/machine_learning/DCT_Data.txt') #read in the dataset

print(dataset.shape) #print out its structure
print(dataset.head()) #prints 5 of the first parts of dataset
#print(dataset.describe()) #examine statistical details of the dataset
# the input is a 16 feature row vector
# the output is a saliency score

# Use only one feature
#diabetes_X = diabetes_X[:, np.newaxis, 2]

# we want to train on these 16 features
#inputTest_X = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[12,2,3,4,5,6,7,8,9,140,11,12,13,114,15,16],[1,2,3,42,5,6,7,8,9,10,11,12,14,14,15,119]]
#inputTest_X = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]
#outputTest_Y = [[0.082],[0.012],[0.05],[0.082],[0.012]]

# for loop to fill the inputTest_X
# we have to add each row to a list, so we will have a list of arrays
# here we read in the data
inputTest_X = []


# read in all the data from DCT_Data.txt
#with open('DCT_Data.txt') as f:
#	for item in f:
#		inputTest_X.append([float(i) for i in item.split()])
#print (inputTest_X)
#inputTest_X = np.concatenate(inputTest_X, axis=0) #concatenates the data

#this below ingestion method does not work properly, but the above works, but it works wrongly
dctFile = open('DCT_Data.txt')
lines1 = dctFile.readlines()
for line in lines1:
	dctList = line.strip().split(' ')
	macroblock = []
	macroblock = np.array(macroblock)
	for i in range(16):
		macroblockValue = float(dctList[i])
		macroblock = macroblock.np.concatenate(macroblockValue, axis=0)
	inputTest_X = np.append(macroblock) 

print (inputTest_X[0])
print (inputTest_X[15])
print (inputTest_X[200000])


# we will have a list of each saliency score
# here we read in the data
saliencyFile = open('saliencyData.txt','r') #read in saliency data
saliencyString = ""

outputTest_Y = [] #initializing saliency list

# we are trying to append all of the saliency scores to outputTest_Y
#with open('saliencyData.txt') as f2:
#	for item in f2:
#		outputTest_Y.append([float(i) for i in item.split()])
#print (inputTest_X)
#outputTest_Y = np.concatenate(outputTest_Y, axis=0) #concatenates the data


#salFile = open('saliencyData.txt')
#lines2 = salFile.readlines()
#for line in lines2:
#	saliencyString = float(line) #converts saliency string to float
#	outputTest_Y.append(saliencyString) #appends saliency string to saliency list

#print(outputTest_Y[0])
#print(outputTest_Y[10])

#for j in range(0,36000):
#    count = 0
#    saliencyString = saliencyFile.readline() #reads in the Saliency Data lines
#    saliencyString = float(saliencyString)
#    outputTest_Y.append(saliencyString)
		    
#    count+=1
#print(outputTest_Y[1])
#print(outputTest_Y[30])

# create linear regression object test
#inputTest_X = np.array(inputTest_X).reshape((36000,16)) #reshape the data to how many rows of DCT macroblocks you have
#regrTest = linear_model.LinearRegression()
#regrTest.fit(inputTest_X,outputTest_Y)

# prediction test data
#inputPred_X = [[28,28,32,32,28,28,32,32,32,32,32,32,32,40,32,40],[-4,-4,-16,-16,-4,-4,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16],[0,0,0,0,0,8,0,6,4,4,23,24,4,4,24,24]]
#outputPred_Y = regrTest.predict(inputPred_X)
#print("Output: \n")
#print(outputPred_Y)

# The coefficients
#print('Coefficients: \n', regrTest.coef_)
# The mean squared error
#print('Mean squared error: %.2f'
#      % mean_squared_error(outputTest_Y, outputTest_Y))
# The coefficient of determination: 1 is perfect prediction
#print('Coefficient of determination: %.2f'
#      % r2_score(outputTest_Y, outputTest_Y))

#plt.scatter(inputTest_X, outputTest_Y,  color='black')
#plt.plot(inputTest_X, outputPred_Y, color='blue', linewidth=3)
#plt.show()

#y = mx1 + mx2 + mx3 + ... mx16 + b

#################################################


# Split the data into training/testing sets
#diabetes_X_train = diabetes_X[:-20]
#diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing set
#diabetes_y_train = diabetes_y[:-20]
#diabetes_y_test = diabetes_y[-20:]

# Create linear regression object
#regr = linear_model.LinearRegression()

# Train the model using the training sets
#regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
#diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
#print('Coefficients: \n', regr.coef_)
# The mean squared error
#print('Mean squared error: %.2f'
#      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# The coefficient of determination: 1 is perfect prediction
#print('Coefficient of determination: %.2f'
#      % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
#plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
#plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

#plt.xticks(())
#plt.yticks(())

#plt.show()
