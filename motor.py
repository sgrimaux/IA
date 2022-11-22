import cv2
import numpy as nump
imgcirculos = cv2.imread('motor.png')
cv2.imshow('Original', imgcirculos)
cv2.waitKey()
# Convertir a escala de grises
imggris = cv2.cvtColor(imgcirculos, cv2.COLOR_BGR2GRAY)
#Difuminar imagen para eliminar ruido y evitar circulos no deseados
sinruido = cv2.medianBlur(imggris,5)
cv2.imshow('Imagen sin ruido', sinruido)
cv2.waitKey()
#Aplicar transformada de Hough para circulos
circulos = cv2.HoughCircles(sinruido, cv2.HOUGH_GRADIENT, 1, 40, param1=95, param2=125, minRadius=0, maxRadius=0)
# Dibujar circulos
if circulos is not None:
    circulos = nump.uint16(nump.around(circulos))
    for i in circulos[0, :]:
        # Círculo exterior
        cv2.circle(imgcirculos, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Centro del círculo
        cv2.circle(imgcirculos, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('circulos detectados', imgcirculos)
cv2.waitKey()