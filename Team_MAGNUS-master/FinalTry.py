import cv2
from time import sleep
from urllib.request import urlopen
import numpy as np
import sys
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    fc=cv2.CascadeClassifier('C:\\Project\\DevSoc19\\haarcascade_frontalface_default.xml')
    ret,frame=cap.read()
    #locx=int(frame.shape[1]/2)
    #locy=int(frame.shape[0]/2)
    frame=cv2.flip(frame,1)
#    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    Error in recognizing!!
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        continue
    try:
        faces=fc.detectMultiScale(gray)
        #cv2.imshow('Original',frame)
        #print("Type => ",type(faces),"\nFaces =>",faces,"\nShape =>",faces.shape)
    #  ERRORRRRRRR!!!!!!!!!!!!!!!!!  --- Need to resolve L8R
        print("Population Density => ",str(faces.shape[0]))
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,100,0),1)
        cv2.rectangle(frame,((0,frame.shape[0]-25)),(270, frame.shape[0]), (255,255,255), -1)
    #Position of people:::
        #cv2.putText(frame, "Number of people: " + str(faces.shape[0]), (0,frame.shape[0] -10), cv2.FONT_ITALIC, 0.5, (0,0,0), 1)
    #Sending data to thingspeak
        fout=urlopen('http://api.thingspeak.com/update?api_key=B2F8ADNONLF1YNJK&field1='+str(faces.shape[0]))
        fout.read()
        fout.close()
        cv2.imshow('Density',frame)
        #cv2.putText(frame, " Detection off ", (locx,locy), cv2.FONT_HERSHEY_PLAIN, 4,  (100,0,255));
        print("Upload Successful!")
    except AttributeError:
        print("~~ No person in scope !!!~~")
        a=0
        fout=urlopen('http://api.thingspeak.com/update?api_key=B2F8ADNONLF1YNJK&field1='+str(a))
        fout.read()
        fout.close()
        continue
    #cv2.waitkey(3000)
    #time.sleep(2)          #Too much laggy --Need 2 remove L8R
    #finally:               #Not necessary
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
