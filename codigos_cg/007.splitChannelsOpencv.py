import numpy as np
import cv2

# ler uma imagem
imagem = cv2.imread('lena.png')

# exibe a imagem em uma janela
cv2.imshow('Imagem',imagem)
cv2.waitKey(0)

# gerar (split) canais RGB, o opencv armazena na ordem BGR
(B, G, R) = cv2.split(imagem)
#cv2.imshow('Vermelho ',R)
#cv2.imshow('Verde',G)
#cv2.imshow('Azul',B)
#cv2.waitKey(0)

# Mostramos as imagens de forma individual
resultado = np.hstack([R, G, B])
cv2.imshow('Vermelho - Verde - Azul',resultado)
cv2.waitKey(0)

# destruir janelas
cv2.destroyAllWindows()


# juntar (merge) as imagens de cada canal
cv2.imshow('Imagem merged',cv2.merge([B, G, R]))
cv2.waitKey(0)

# criar uma imagem colorida por cada canal
zeros = np.zeros(imagem.shape[:2], dtype="uint8")
#cv2.imshow('Vermelho ',cv2.merge([zeros, zeros, R]))
#cv2.imshow('Verde ',cv2.merge([zeros, G, zeros]))
#cv2.imshow('Azul ',cv2.merge([B, zeros, zeros]))
#cv2.waitKey(0)

# Mostramos os canais individuais na forma BGR
resultado = np.hstack([
                cv2.merge([zeros, zeros, R]),
                cv2.merge([zeros, G, zeros]),
                cv2.merge([B, zeros, zeros])])
cv2.imshow('Vermelho - Verde - Azul',resultado)
cv2.waitKey(0)

# destruir janelas
cv2.destroyAllWindows()