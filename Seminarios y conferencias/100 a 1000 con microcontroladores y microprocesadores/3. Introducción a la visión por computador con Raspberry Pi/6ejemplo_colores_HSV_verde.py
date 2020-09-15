#!/usr/bin/env python3
import numpy as np
import cv2


imagen = cv2.imread('colores.jpg')
cv2.imshow('imagen RGB',imagen)


imagenHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)

minVerde = np.array([40,0,0])
MaxVerde = np.array([80,255,255])
Verde=cv2.inRange(imagenHSV,minVerde,MaxVerde)
cv2.imshow('Verde',Verde)
cv2.waitKey(0)
cv2.destroyAllWindows()


