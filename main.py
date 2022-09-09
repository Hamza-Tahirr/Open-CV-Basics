import cv2
import numpy as np

#Reading an image
img = cv2.imread("img/fruits.jpg")
print(img.shape)


# For showing an image 
cv2.imshow('window',img)
cv2.waitKey(0)  #this shows the pic will be there for infinite time untill u cross


#Converting color pics into greyscale
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('window',img_grey)
cv2.waitKey(0) 
print(img_grey.shape)


#Playing with rgb

imgBLUE= img[:,:,0]
imgGREEN= img[:,:,1]
imgRED= img[:,:,2]

new_img = np.hstack((imgBLUE,imgGREEN,imgRED))

cv2.imshow('window',new_img)
cv2.waitKey(0) 



#Resizing the Image
img = cv2.imread("img/fruits.jpg")
img_resize=cv2.resize(img,(500,500))
for resizing to half 
img_resize=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
cv2.imshow("window",img)
cv2.waitKey(0)
print(img_resize.shape)


#Flipping the image 
img = cv2.imread("img/fruits.jpg")
img_flip=cv2.flip(img,0) #vertical flip
img_flip=cv2.flip(img,1) #horiontal flip
img_flip1=cv2.flip(img,-1) #both horizontal and vertical
cv2.imshow("window",img_flip1)
cv2.waitKey(0)



#Cropping An Image
img = cv2.imread("img/fruits.jpg")
img_crop = img[100:300,200:500]
cv2.imshow("window",img_crop)
cv2.waitKey(0)


#Saving an image 
img = cv2.imread("img/fruits.jpg")
img_crop = img[100:300,200:500]
cv2.imwrite('fruits_small.png',imp_crop)
cv2.imshow("window",img_crop)
cv2.waitKey(0)


#Drawing Shapes 
## creating own image
img=np.zeros((512,512,3))
##For rectangle
cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=3)
##For Circle
cv2.circle(img,center=(100,300),radius=50,color=(0,0,255),thickness=3)
##For Line
cv2.line(img,pt1=(0,0),pt2=(200,200),color=(255,0,0),thickness=2)
##Text
cv2.putText(img,org=(100,100),fontScale=4,color=(0,255,255),thickness=2,lineType=cv2.LINE_AA,text="Hamza",fontFace=cv2.FONT_ITALIC)
cv2.imshow("window",img)
cv2.waitKey(0)




#Live Direct Drawing
#EVENTS ---- CLICKS OR ANYTHING ELSE

def draw(event,x,y,flags,params):
    if event ==1: #mouse click  hwa
        cv2.circle(img,center=(x,y),radius=50,color=(0,0,255),thickness=-1)
        
cv2.namedWindow(winname='window')
cv2.setMouseCallback('window',draw)

img = np.zeros((512,512,3))

while True:
    cv2.imshow('window',img)
    if cv2.waitKey(1) & 0xFF== ord('x'): #x will break down our screen if we press x
        break

cv2.destroyAllWindows()

##For making a rectangle while streching using 3 mouse events 
flag =False
ix=-1
iy=-1

def draw(event,x,y,flags,params):
    global flag,ix,iy

    if event == 1: #mouse click  hwa
       flag = True
       ix=x
       iy=y

    elif event == 0:
        if flag==True:
            cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,255),thickness=-1)

    elif event == 4:
        flag=False 
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,255),thickness=-1)

cv2.namedWindow(winname='window')
cv2.setMouseCallback('window',draw)

img = np.zeros((512,512,3))

while True:
    cv2.imshow('window',img)
    if cv2.waitKey(1) & 0xFF== ord('x'): #x will break down our screen if we press x
        break

cv2.destroyAllWindows()

