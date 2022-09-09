from tkinter import Frame
import cv2
import numpy as np
import time


cap=cv2.VideoCapture(0) #0 stand for primary webcamp


while True:

    ret, frame = cap.read()
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('webcam',img_gray) # shwoing screen

    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break

cv2.destroyAllWindows()    



##FOR WEBCAM RECORDING :

cap=cv2.VideoCapture(0) #0 stand for primary webcamp
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,488))

while True:

    ret, frame = cap.read()
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(img_gray)
    cv2.imshow('webcam',img_gray) # shwoing screen

    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break
out.release()
cv2.destroyAllWindows()    



##For playing a Video


cap=cv2.VideoCapture('output.avi') #0 stand for primary webcamp


while True:

    ret, frame = cap.read()
    time.sleep(1/20)        # from time library 
    cv2.imshow('webcam',img_gray) # shwoing screen

    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break

cv2.destroyAllWindows()    


