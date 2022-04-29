#Profa. Edhelmira Lima;
#Data: 26-10-2021
#Exemplo: Código base para calcular o histograma para uma imagem em tons de cinza

import cv2
from matplotlib import pyplot as plt

# ler uma imagem
imagem = cv2.imread('lena.png')
# exibe a imagem em uma janela
cv2.imshow('Imagem original',imagem)

# criar imagem em tons de cinza
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem tons de cinza',imagemCinza)

# calcular o histograma para imagem em tons de cinza
histograma = cv2.calcHist([imagemCinza],[0],None,[256],[0,256])

# mostrar o histograma
plt.figure()
plt.title("Histograma tons de cinza")
plt.xlabel("Intensidade")
plt.ylabel("Número de pixels")
plt.plot(histograma)
plt.xlim([0, 256])
plt.show()

# calcular o histograma de uma imagem rgb
channel = cv2.split(imagem)
cores = ("b", "g", "r")

# mostrar o histograma
plt.figure()
plt.title("Histograma rgb")
plt.xlabel("Intensidade")
plt.ylabel("Número de pixels")
for (canal, cor) in zip(channel, cores):
    histogramaRGB = cv2.calcHist([canal],[0],None,[256],[0,256])
    plt.plot(histogramaRGB, color=cor)
    plt.xlim([0, 256])
    
