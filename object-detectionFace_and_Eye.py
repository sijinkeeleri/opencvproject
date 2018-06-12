import cv2 
import numpy as np 

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# watch_cascade = cv2.CascadeClassifier('params.xml')

cap = cv2.VideoCapture('video/Face Test.mp4')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # watches = watch_cascade.detectMultiScale(gray, 1.3, 5)
    # for (x,y,w,h) in watches:
    #     cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0.0), 2)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w-2, y+h-2), (255,255.0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew-2,ey+eh-2), (0,0,255), 2)
        
    cv2.imshow('frame', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

        cap.release()
        cv2.destroyAllWindows()
