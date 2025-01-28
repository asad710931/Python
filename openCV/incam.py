import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    #cv2.imshow('frame',frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret:
        for i in range(4):
            if i==1:
                cv2.imshow('frame1',gray)
            else:
                cv2.imshow(f'frame{i}',frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break