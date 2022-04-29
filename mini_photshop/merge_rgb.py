import numpy as np
import cv2
import os
# Abrir imagem
imagem = cv2.imread(os.path.expanduser( "~/Downloads/floresta.png"))

cv2.imshow('Image', imagem)
cv2.waitKey(0)

(B, G, R) = cv2.split(imagem)

resultado = np.hstack([R, G, B])
cv2.imshow('Vermelho - verde - azul', resultado)
cv2.waitKey(0)

#black and white --------------------
cv2.imwrite(os.path.expanduser( "~/Downloads/floresta2.png"), resultado)

cv2.imshow('Imagem Merged', cv2.merge([B, G, R]))
cv2.waitKey(0)

zeros = np.zeros(imagem.shape[:2], dtype="uint8")

resultado = np.hstack([
    cv2.merge([zeros, zeros, R]),
    cv2.merge([zeros, G, zeros]),
    cv2.merge([B, zeros, zeros]),
])

cv2.imshow('Imagem Merged', resultado)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Fim abrir uma imagem

