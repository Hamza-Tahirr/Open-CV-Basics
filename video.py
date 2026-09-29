import cv2
import time


cap=cv2.VideoCapture(0) #0 stands for primary webcam


while True:

    ret, frame = cap.read()
    if not ret:
        break
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('webcam',img_gray) # showing screen

    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break

cap.release()
cv2.destroyAllWindows()



##FOR WEBCAM RECORDING :

cap=cv2.VideoCapture(0) #0 stands for primary webcam
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#size has to match the camera, isColor=False for gray frames
out=cv2.VideoWriter('output.avi',fourcc,20.0,(width,height),isColor=False)

while True:

    ret, frame = cap.read()
    if not ret:
        break
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(img_gray)
    cv2.imshow('webcam',img_gray) # showing screen

    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()



##For playing a Video


cap=cv2.VideoCapture('output.avi')


while True:

    ret, frame = cap.read()
    if not ret:
        break
    time.sleep(1/20)        # from time library
    cv2.imshow('video',frame)

    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break

cap.release()
cv2.destroyAllWindows()
