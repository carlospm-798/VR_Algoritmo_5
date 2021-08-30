#Carlos Paredes Márquez
#Ejercicio dos
#29 08 2021

import cv2
import matplotlib.pyplot as plt

'''Paso uno'''
ig = cv2.imread('Sakura.jpg',0)
ig = cv2.resize(ig, None, fx=0.25, fy=0.25)
[M,N] = ig.shape[0:2]

'''Paso dos'''
ig2 = cv2.multiply(ig, 0.5)
ig2 = cv2.add(ig2, 2)
[O,P] = ig2.shape[0:2]

'''Paso cinco.uno'''
ig3 = cv2.multiply(ig, 0.9)
ig3 = cv2.add(ig3, 1.5)
[Q,R] = ig3.shape[0:2]

'''Paso cinco.dos'''
ig4 = cv2.multiply(ig, 1.7)
ig4 = cv2.add(ig4, 0.25)
[S,T] = ig4.shape[0:2]

'''Paso cinco.tres'''
ig5 = cv2.multiply(ig,2)
ig5 = cv2.add(ig5, 2)
[U,V] = ig5.shape[0:2]

'''Calculo de histograma'''
hist = cv2.calcHist([ig],[0],None,[256],[0,256]).flatten()/(M*N)
hist2 = cv2.calcHist([ig2],[0],None,[256],[0,256]).flatten()/(O*P)
hist3 = cv2.calcHist([ig3],[0],None,[256],[0,256]).flatten()/(Q*R)
hist4 = cv2.calcHist([ig4],[0],None,[256],[0,256]).flatten()/(S*T)
hist5 = cv2.calcHist([ig5],[0],None,[256],[0,256]).flatten()/(U*V)

'''Ecualización de imagenes'''
im_eq = cv2.equalizeHist(ig2)
im_eq2 = cv2.equalizeHist(ig3)
im_eq3 = cv2.equalizeHist(ig4)
im_eq4 = cv2.equalizeHist(ig5)

cv2.imshow('image1',ig)
cv2.imshow('image2',ig2)
cv2.imshow('image3',ig3)
cv2.imshow('image4',ig4)
cv2.imshow('image4',ig5)
cv2.imshow('Ecualizado_im2',im_eq)
cv2.imshow('Ecualizado_im3',im_eq2)
cv2.imshow('Ecualizado_im4',im_eq3)
cv2.imshow('Ecualizado_im4',im_eq4)

'''Hist-1'''
fig= plt.figure()
plt.bar(range(len(hist)),hist)
'''Hist-2'''
fig2= plt.figure()
plt.bar(range(len(hist2)),hist2)
'''Hist-3'''
fig3= plt.figure()
plt.bar(range(len(hist3)),hist3)
'''Hist-4'''
fig4 = plt.figure()
plt.bar(range(len(hist4)),hist4)
'''Hist-5'''
fig5 = plt.figure()
plt.bar(range(len(hist5)),hist5)
'''Mostrar'''
plt.show()