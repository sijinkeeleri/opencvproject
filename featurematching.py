import numpy as np 
import cv2 as cv 
from matplotlib import pyplot as plt 

img1 = cv.imread('images/opencv-feature-matching-template.jpg', 0)
img2 = cv.imread('images/opencv-feature-matching-image.jpg', 0)

orb = cv.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x:x.distance)

img3 = cv.drawMatches(img1,kp1,img2,kp2, matches[:13], None, flags=2)
plt.imshow(img3)
plt.show() 