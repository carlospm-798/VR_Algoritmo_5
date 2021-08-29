#Carlos Paredes Márquez
#Cambiar el tamaño de una imagen
#29 08 2021

import cv2

im = cv2.imread('Sasuke.png')
print(im.shape) # (674, 1199, 3)

'''Si la escala < 1, encoje.  > 1 crece'''
#im2 = cv2.resize(im, (600, 400)) #ancho, altura
im2 = cv2.resize(im, None, fx=0.5, fy=0.5) #dar escala de recorte
print(im2.shape)

cv2.imshow('Image0', im)
cv2.imshow('Image1', im2)
cv2.waitKey(0)