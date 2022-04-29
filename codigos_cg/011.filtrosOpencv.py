#Profa. Edhelmira Lima;
#Data: 03-12-2021
#Exemplo: Código de equalização de histogramas

import cv2
import numpy as np

# ler uma imagem
imagem = cv2.imread('lena.png')

# exibe a imagem em uma janela
cv2.imshow('Imagem original',imagem)
cv2.waitKey(0)

# Aplica o filtro da média com diferentes máscaras
# Empilha resultados lado a lado
media = np.hstack([
    cv2.blur(imagem,(3,3)),
    cv2.blur(imagem,(5,5)),
    cv2.blur(imagem,(7,7))])
cv2.imshow('Filtro média',media)
cv2.waitKey(0)

# filtro mediana com diferentes máscaras
# Empilha resultados lado a lado
mediana= np.hstack([
    cv2.medianBlur(imagem,3),
    cv2.medianBlur(imagem,5),
    cv2.medianBlur(imagem,7)])

cv2.imshow('Filtro mediana',mediana)
cv2.waitKey(0)

# filtro gaussiano com diferentes máscaras
# Empilha resultados lado a lado
gauss= np.hstack([
    cv2.GaussianBlur(imagem,(3,3),0),
    cv2.GaussianBlur(imagem,(5,5),0),
    cv2.GaussianBlur(imagem,(7,7),0)])

cv2.imshow('Filtro gaussiano',gauss)
cv2.waitKey(0)


# filtro canny
# Empilha resultados lado a lado
imagemFiltrada = cv2.GaussianBlur(imagem, (3, 3), 0)
canny = cv2.Canny(imagemFiltrada, 100, 200)
cv2.imshow('Filtro canny',canny)
cv2.waitKey(0)

cv2.destroyAllWindows()