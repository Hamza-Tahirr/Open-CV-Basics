import sys

import cv2

path = sys.argv[1] if len(sys.argv) > 1 else "img/fruits.jpg"

img = cv2.imread(path)
if img is None:
    sys.exit(f"Could not read image: {path}")
original = img.copy()

ix=-1
iy=-1


def crop(event,x,y,flags,params):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDOWN:
        ix=x
        iy=y
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,0),thickness=1)
        #Crop tools
        x1,x2 = sorted((max(ix,0),max(x,0)))
        y1,y2 = sorted((max(iy,0),max(y,0)))
        cropped= original[y1:y2,x1:x2]
        if cropped.size:
            cv2.imshow("new_window",cropped)


cv2.namedWindow(winname='window')
cv2.setMouseCallback('window',crop)

while True:

    cv2.imshow('window',img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
