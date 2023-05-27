import numpy as np
import cv2
from numpy import shape
import random

def gaosi(src,means,sigma,percetage):
    Noiseimg=src
    Noisenum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(Noisenum):
        randX=random.randint(0,src.shape[0]-1)
        randY=random.randint(0,src.shape[1]-1)
        Noiseimg[randX,randY]=Noiseimg[randX,randY]+random.gauss(means,sigma)
        if Noiseimg[randX,randY] < 0:
           Noiseimg[randX,randY] = 0
        elif Noiseimg[randX,randY] > 255:
             Noiseimg[randX,randY] = 255
    return Noiseimg

img = cv2.imread('lenna.png',0)
imggaosi= gaosi(img,2,4,0.8)
img = cv2.imread('lenna.png')
imgsrc=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('source',imgsrc)
cv2.imshow('lenna_gaosiNoise',imggaosi)
cv2.waitKey(0)