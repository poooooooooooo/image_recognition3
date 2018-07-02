import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('image')

cv2.createTrackbar('filt','image',1,10,nothing)

cv2.createTrackbar('value','image',0,100,nothing)

cv2.createTrackbar('R','image',0,200,nothing)
cv2.createTrackbar('G','image',0,200,nothing)
cv2.createTrackbar('B','image',0,200,nothing)

cv2.setTrackbarPos('R','image',100)
cv2.setTrackbarPos('G','image',100)
cv2.setTrackbarPos('B','image',100)

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

while(1):
    ret,frame=cap.read()
    if not ret:
        continue

    gamma=cv2.getTrackbarPos('value','image')*0.1
    if gamma == 0:
        gamma = 0.1

    LUT=np.zeros((256,1),dtype='uint8')
    for i in range(256):
        LUT[i][0] = 255*pow(float(i)/255,1.0/gamma)

    frame = cv2.LUT(frame,LUT)
    print(frame)

    r = cv2.getTrackbarPos('R','image')/100
    g = cv2.getTrackbarPos('G','image')/100
    b = cv2.getTrackbarPos('B','image')/100

    frame = frame/255
    frame[:,:,2] *= r
    frame[:,:,1] *= g
    frame[:,:,0] *= b

    v = cv2.getTrackbarPos('filt','image')
    frame = cv2.GaussianBlur(frame,(25,25),v)

    cv2.imshow('image',frame)
    k=cv2.waitKey(1)&0xFF
    if k==ord('q') or k==27:
        break

cap.release()
cv2.destroyAllWindows()
