import cv2
import numpy as nump

imgOrig = cv2.imread('ruta1.png')
cv2.imshow('Imagen original', imgOrig)
cv2.waitKey()

gris = cv2.cvtColor(imgOrig, cv2.COLOR_BGR2GRAY)

bordes = cv2.Canny(gris, 150, 500, apertureSize = 3, L2gradient=False)
lineas = cv2.HoughLinesP(bordes, 1, nump.pi/180, 40, minLineLength=0, maxLineGap=60)

if lineas is not None:
    for linea in lineas:
        x1, y1, x2, y2 = linea[0]
        #dibujo lineas
        cv2.line(imgOrig, (x1,y1), (x2,y2), (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('Bordes de Imagen limpia', bordes)
cv2.waitKey()
cv2.imshow('Lineas detectadas en la imagen original', imgOrig)
cv2.waitKey()
