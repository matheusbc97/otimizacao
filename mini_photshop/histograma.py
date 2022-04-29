import cv2
from cv2 import cvtColor
import os
from matplotlib import pyplot as plt

imagem = cv2.imread(os.path.expanduser( "~/Downloads/floresta.png"))
cv2.imshow('Imagem Originial', imagem)


imagemCinza = cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem Tons de cinza', imagemCinza)

histograma = cv2.calcHist([imagemCinza], [0], None, [256], [0,256])

plt.figure()
plt.title("Histograma de tons de cinza")
plt.xlabel("Itensidade")
plt.ylabel("Número de pixels")
plt.plot(histograma)
plt.xlim([0, 256])
plt.show()