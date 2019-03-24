import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    roi=frame[100:900, 100:900]
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame',frame)
    fr=frame
    sift=cv2.xfeatures2d.SIFT_CREATE(fr,None)
    kp=sift.detect(fr,None)
    fr=cv2.drawKeyPoints(fr,kp,None)
    cv2.imshow('Keypoints',fr)
    lower_lim = np.array([0,20,70], dtype=np.uint8)
    upper_lim = np.array([20,255,255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_lim, upper_lim)
    mask = cv2.GaussianBlur(mask,(5,5),100)
    cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
