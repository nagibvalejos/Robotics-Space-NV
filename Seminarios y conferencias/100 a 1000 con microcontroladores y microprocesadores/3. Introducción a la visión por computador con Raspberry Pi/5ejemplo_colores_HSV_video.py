import numpy as np
import cv2

cap= cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    
    cv2.imshow('imagen RGB', frame)
    imagenHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    minColor = np.array([115,50,50])
    maxColor = np.array([125,255,255])
    mascara = cv2.inRange(imagenHSV, minColor, maxColor)
    res = cv2.bitwise_and(frame,frame, mask= mascara)

    cv2.imshow('mask',mascara)
    cv2.imshow('res',res)

    if cv2.waitKey(1)==ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
