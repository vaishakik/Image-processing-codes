# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 07:22:44 2018

@author: Dikshit Hegde
"""
import numpy as np
import cv2
img1 = cv2.imread('lena.jpg')
img = cv2.imread('lena.jpg')
cv2.imshow('before',img1)
cv2.imshow('after',img)
b = cv2.waitKey(0)
if b == 27:
    cv2.destroyAllWindows()

h = np.zeros([3,3],np.uint8)
m = np.size(img,1)
n = np.size(img,0)
for i  in range(m):
    for j in range(n):
        if(i+2 < m and j+2 <n):
            for k in range(3):
                for l in range(3):
                    h[k,l] = img[(i+k),(j+l)]
            a = 0
            for k in range(3):
                for l in range(3):
                    a = a + h[k,l]
            
            a = a / 9
            for k in range(3):
                for l in range(3):
                    img[i+k,l+j] = a

img = np.uint8(img)
cv2.imshow('before',img1)
cv2.imshow('after',img)
b = cv2.waitKey(0)
if b == 27:
    cv2.destroyAllWindows()

        