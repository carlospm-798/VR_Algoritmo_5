#Carlos Paredes Márquez
#Ejercicio uno, ecualizar una imagen
#29 08 2021

import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread('Sasuke.png',0)
[M,N] = im.shape[0:2]

im2 = cv2.resize(im, None, fx=0.5, fy=0.5)
[O,P] = im2.shape[0:2]

im3 = cv2.resize(im, None, fx=0.25, fy=0.25)
[Q,R] = im3.shape[0:2]

#im2 = cv2.multiply(im, 0.5) #disminuir el brillo en escala gris
#im3 = cv2.add(im, 20) #agregar brillo en escala de grises

hist = cv2.calcHist([im],[0],None,[256],[0,256]).flatten()/(M*N) #/(M*N) para calcular la normalización
hist2 = cv2.calcHist([im2],[0],None,[256],[0,256]).flatten()/(O*P)
hist3 = cv2.calcHist([im3],[0],None,[256],[0,256]).flatten()/(Q*R)
#im_equ = cv2.equalizeHist(im)

cv2.imshow('Image1', im)
cv2.imshow('Image2', im2)
cv2.imshow('Image3',im3)

'''Histo-1'''
fig= plt.figure()
plt.bar(range(len(hist)),hist)
'''Histo-2'''
fig2= plt.figure()
plt.bar(range(len(hist2)),hist2)
'''Histo-3'''
fig3= plt.figure()
plt.bar(range(len(hist3)),hist3)
'''Mostrar'''
plt.show()
#cv2.waitKey(0)