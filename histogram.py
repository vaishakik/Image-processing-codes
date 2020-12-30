# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 05:53:50 2018

@author: dell
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
img1 = cv2.imread('lena.jpg',0)
img = cv2.imread('lena.jpg',0)
hist = np.zeros([256])
x = np.linspace(0,1,256)
m = np.size(img,1)
n = np.size(img,0)
for i in range(m):
    for j in range(n):
        hist[(img[i,j])] = hist[(img[i,j])] + 1
plt.figure(1)
plt.plot(x,hist)
for i in range(256):
    hist[i] = hist[i]/(m*n)

for i in range(256):
    if i != 0:
        hist[i] = hist[i-1]+hist[i]

for i in range(256):
	hist[i] = hist[i] * 256

for i in range(m):
	for j in range(n):
		img1[i,j] = hist[img1[i,j]]

img1 = np.uint8(img1)
hist1 = np.zeros(256)
for i in range(m):
    for j in range(n):
        hist1[(img1[i,j])] = hist1[(img1[i,j])] + 1

plt.figure(2)
plt.plot(x,hist1)
#cv2.imshow('new',img1)
#cv2.imshow('old',img)
#k = cv2.waitKey(0)
#if k == 27:
#    cv2.destroyAllWindows()
