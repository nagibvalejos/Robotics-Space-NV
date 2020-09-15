import cv2
import numpy as np

##Creacion de una imagen en escala de grises
#img=np.zeros((512,512),np.uint8)
##Creacion de una imagen en espacio RGB
img=np.zeros((512,512,3),np.uint8)
#print(img)
##Se da color a la imagen
img[:]=128,128,128
#img[100:200,200:400]=255,0,0

#crear linea
#cv2.line(img,(0,0),(300,300),(0,255,0),3)#el ultimo 3 es el grosor de la linea
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

#crear rectangulo
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)

#crear circulo
cv2.circle(img,(300,100),40,(100,80,200),2)

#poner texto
cv2.putText(img,'OpenCV', (300,100),cv2.FONT_HERSHEY_COMPLEX,1,(200,0,0),1)#PRIMER 1 ESCALA, segundo grosor de linea

cv2.imshow('Imagen Creada',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
