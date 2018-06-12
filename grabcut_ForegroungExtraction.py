import numpy as np 
import cv2 

from matplotlib import pyplot as plt 

img = cv2.imread('images/opencv-python-foreground-extraction-tutorial.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50, 50, 250, 350)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,9,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

cv2.imshow('grab', img)
# plt.colorbar()
# plt.show() 
cv2.waitKey(0)
cv2.destroyAllWindows()
