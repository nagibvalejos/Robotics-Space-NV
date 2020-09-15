#!/usr/bin/env python3
import cv2
##carga la imagen
##segundo argumento puede ser 1(color), 0(escala de grises) y -1 (sin cambios)
img=cv2.imread('lena.jpg',0)
#Muestra la imagen
cv2.imshow('Lena', img)
##Guardar la imagen
cv2.imwrite('lena_grises.png',img)
#se anade un delay en milisegundos para la ventana
#se pone 0 para que sea indefinido
#y se presiona cualquier tecla para salir
#si la maquina es de 64 bits poner cv2.waitKey(0) & 0xFF
cv2.waitKey(0)
##cierra todas las ventanas
cv2.destroyAllWindows() 