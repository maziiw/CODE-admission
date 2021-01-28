import os
import caer
#import canaro
#import numpy as np
#import gc
import cv2.cv2 as cv

#img = cv.imread('c1.jpg')
# cv.imshow('capture',img)
cv.waitKey(0)

IMG_SIZE(80,80)
channels = 1
char_path = r'/Users/marz/Git/CODE-admission/modelling/images'

char_dict={}
for char in os.listdir(char_path):
    char_dict[char]=len(os.listdir(os.path.join(char_path,char)))

char_dict=caer.sort_dict(char_dict,descending=True)
char_dict