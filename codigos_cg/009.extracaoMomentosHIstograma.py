#Profa. Edhelmira Lima;
#Data: 26-10-2021
#Exemplo: Código para determinar os momentos estatísticos

# importar a bibliotecas
import scipy.stats as stats
import numpy as np
import cv2

# ler uma imagem
imagem = cv2.imread('lena.png')

# exibe a imagem em uma janela
cv2.imshow('Imagem original',imagem)
#cv2.waitKey(0)

# criar imagem em tons de cinza
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem tons de cinza',imagemCinza)
#cv2.waitKey(0)

# calcular o histograma para imagem em tons de cinza
histograma = cv2.calcHist([imagemCinza],[0],None,[256],[0,256])

# Criamos um vetor de características e inicializamos com 0s
caracteristicas = np.zeros(4)

# Calculamos os momentos estatísticos e adicionamos ao vetor de características
caracteristicas[0] = histograma.mean() # media
caracteristicas[1] = histograma.std() # desvio padrão
caracteristicas[2] = stats.kurtosis(histograma) # curtose
caracteristicas[3] = stats.skew(histograma) # obliquidade

#Mostramos o vetor de características
print(caracteristicas)