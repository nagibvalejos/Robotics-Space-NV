#!/usr/bin/env python3
import cv2
import numpy
import time

img= cv2.imread('lena.jpg')
##se imprime las dimensiones de la imagen
print(img.shape)
##Redimensionamiento de la imagen se puede realizar de cualquiera de las dos maneras
#img_r=cv2.resize(img,None,fx=0.5,fy=0.5)
#img_r=cv2.resize(img,(320,240))
print(img_r.shape)
##Se descompone las imagenes
B, G, R= cv2.split(img_r)
##Otra opcion para descomponer
#B=img[:,:,0]
#G=img[:,:,1]
#R=img[:,:,2]

#img_Recortada=img[0:100,100:200]
#cv2.imshow('Azul',B)
#cv2.imshow('Verde',G)
#cv2.imshow('Rojo',R)
#concat solo puede concatenar arreglos con el mismo espacio de color
#final=cv2.vconcat([B,G,R])
final=cv2.hconcat([B,G,R])
#stack apila arreglos con la misma cantidad de espacios de color
#hor=np.hstack((R,G,B))
#ver=np.vstack((R,G,B))

cv2.imshow('Azul - Verde - Rojo', final)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
##Para video
cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    frame_r=cv2.resize(frame,None,fx=0.5,fy=0.5)
    B,G,R=cv2.split(frame_r)
    total=cv2.hconcat([B,G,R])
    cv2.imshow('Video',total)

    if cv2.waitKey(1)== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''     
