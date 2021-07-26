#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This is going to attach the saliency scores from "SaliencyData.txt" onto the DCT_Data file
It is non-destructive and creates a new file.
"""

import shutil

# pseudo-code for combining the data

# import the SaliencyData.txt file so its contents can be added
file2 = open('SaliencyData.txt','r')

# copying the DCT files for processing
shutil.copy('/home/alif/machine_learning/DCT_Data.txt', '/home/alif/machine_learning/DCT_With_SaliencyRead.txt')
shutil.copy('/home/alif/machine_learning/DCT_Data.txt', '/home/alif/machine_learning/DCT_With_SaliencyWrite.txt')

# create a new file to read and write all the contents
file3 = open('DCT_With_SaliencyRead.txt','r')
file1 = open('DCT_With_SaliencyWrite.txt','w')


stringlist1 = file3.readline() # start reading the DCT data (to be overwritten)
file1.write("saliency, macroblock")

for j in range(0,4500):
    count = 0
    stringlist2 = file2.readline() #reads in the Saliency Data lines
    saliencyData = stringlist2.strip().split(',')
    for i in range(80):
	    saliencyScore = saliencyData[count]
	    stringtoprint =  saliencyScore + stringlist1 
            # fill in missing block indices based on index, read two lines in advance and ask Orren to supply solution
	    file1.write(stringtoprint)
	    count+=1
	    stringlist1 = file3.readline() # reading the file


# newcontents = stringlist1 + stringlist2


# update the DCT_Data file

