import numpy as np 
import cv2

cap = cv2.VideoCapture('video/Color Filtering.mp4')

if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    lower_red = np.array([150,150,50])
    upper_red = np.array([255,255,50])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # applying blur effect 
    kernal = np.ones((15,15), np.float32)/255
    # using filter
    smoothed = cv2.filter2D(res, -1, kernal)
    # using Gaussianblur
    blur = cv2.GaussianBlur(res, (15,15), 0)
    # Using median blur
    median = cv2.medianBlur(res, 15)
    # using bilateral filter
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    

    # cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res',res)
    # cv2.imshow('smoothed',smoothed)
    # cv2.imshow('blur',blur)
    # cv2.imshow('median',median)
    # cv2.imshow('bilateral',bilateral)
 
    # Display the resulting frame
    # cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(2) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
