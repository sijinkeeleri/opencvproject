import numpy as np 
import cv2 as cv 

img= cv.imread('images/watch.jpg', cv.IMREAD_COLOR)
img[55,65] = [0,0,0]


watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face
img[37:111, 107:194] = [255,255,255]
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()

