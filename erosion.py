# -*- coding: utf-8 -*-r
"""
Created on Fri Mar 30 07:02:38 2018

@author: Dikshit Hegde
"""

import numpy as np
import cv2
img1 = cv2.imread(r'C:\Users\Dikshit Hegde\Desktop\summer work shop\basic image\whiteback.png',0)
img = cv2.imread(r'C:\Users\Dikshit Hegde\Desktop\summer work shop\basic image\whiteback.png',0)
ker = np.zeros([3,3],np.uint8)
m = np.size(img,1)
n = np.size(img,0)
for i in range(m-3):
    for j in range(n-3):
        for k in range(3):
            for l in range(3):
                ker[k,l] = img[(i+k),(j+l)]
        flag = 0
        for k in range(3):
            for l in range(3):
                if ker[k,l] == 0:
                    flag = 1
        if flag == 1:              
            for k in range(3):
                for l in range(3):
                    img[(i+k),(j+l)] = 0

img = np.uint8(img)
cv2.imshow('after',img)
cv2.imshow('before',img1)
a = cv2.waitKey(0)
if a == 27:
    cv2.destroyAllWindows()