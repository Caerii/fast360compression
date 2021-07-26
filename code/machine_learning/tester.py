#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

numb_list = []    
with open('data.txt') as f:
    for item in f:
        numb_list.append([int(i) for i in item.split()])
print (numb_list)
print (numb_list[0])  #print list
print ('A number in list 0: %d' % numb_list[0][2])


