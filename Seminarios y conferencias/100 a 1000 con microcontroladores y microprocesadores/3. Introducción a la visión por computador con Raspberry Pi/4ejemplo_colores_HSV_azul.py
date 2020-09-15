import numpy as np
import cv2

## leer imagen 
imagen = cv2.imread('colores.jpg')
cv2.imshow('imagen RGB', imagen)

## convertimos modelo del color a HSV 
imagenHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)

cv2.imshow('imagen HSV', imagenHSV)


## se crean arrays con los valores HSV (o HLS si se esta usando) en el 
## orden respectivo que sean los valores Maximo y minimo a filtrar de la imagen
minColor = np.array([115,0,0])
maxColor = np.array([125,255,255])

## se filtra en una "mascara" los valores que deseamos segmentar
mascara = cv2.inRange(imagenHSV, minColor, maxColor)

## para visualizar a color la imagen con el area de color deseada
## se combina ambas imagenes
res = cv2.bitwise_and(imagen,imagen, mask= mascara)

## se imprimen ambas muestras para ver el proceso
cv2.imshow('mask',mascara)
cv2.imshow('res',res)

## comandos de control para la aplicacion
cv2.waitKey(0)
cv2.destroyAllWindows()
