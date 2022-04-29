import cv2
from cv2 import cvtColor
import os
from matplotlib import pyplot as plt

imagem = cv2.imread(os.path.expanduser( "~/Downloads/floresta.png"))
cv2.imshow('Imagem Originial', imagem)

channel = cv2.split(imagem)
cores = ("b", "g", "r")

plt.figure()
plt.title("Histograma RGB")
plt.xlabel("Itensidade")
plt.ylabel("Número de pixels")

for (canal, cor) in zip(channel, cores):
    histogramaRGB = cv2.calcHist([canal], [0], None, [256], [0,256])
    plt.plot(histogramaRGB, color=cor)
    plt.xlim([0, 256])

plt.show()