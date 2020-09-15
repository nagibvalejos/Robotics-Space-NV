#!/usr/bin/env python3
import cv2
##captura la direccion del video
cap= cv2.VideoCapture(0)
#configuracion de la resolucion de la camara
#cap.set(3,320)#ancho
#cap.set(4,240)#alto 
#cap.set(10,100)#brillo
while True:
	##variable ret booleano que indica si se recibe info del video
	##frame es el cadro del video
	ret, frame= cap.read()	
	##para convertir a escala de grises
	#img_gris= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	##muestra el video
	cv2.imshow('Video',frame)
	##para salir del loop	
	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

