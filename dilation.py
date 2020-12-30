# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 07:02:38 2018

@author: Dikshit Hegde
"""

import numpy as np
import cv2
img1 = cv2.imread('white.jpg')
img = cv2.imread('white.jpg')
ker = np.zeros([3,3])
m = np.size(img,1)
n = np.size(img,0)
for i in range(m):
    for j in range(n):
        if(i+2 < m and j+2 <n):
            for k in range(3):
                for l in range(3):
                    ker[k,l] = img[(i+k),(j+l)]
            
            for k in range(3):
                for l in range(3):
                    if ker[k,l] == 255:
                        flag = 1
            if flag == 1:            
                for k in range(3):
                    for l in range(3):
                        img[(i+k),(j+l)] = 255

img = np.uint8(img)
cv2.imshow('after',img)
cv2.imshow('before',img1)
a = cv2.waitKey(0)
if a == 27:
    cv2.destroyAllWindows()