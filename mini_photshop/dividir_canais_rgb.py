import numpy as np
import cv2
import os
# Abrir imagem
imagem = cv2.imread(os.path.expanduser( "~/Downloads/floresta.png"))

cv2.imshow('Image', imagem)
#cv2.waitKey(0)

(B, G, R) = cv2.split(imagem)

resultado = np.hstack([R, G, B])
cv2.imshow('Vermelho - verde - azul', resultado)
#cv2.waitKey(0)
cv2.imwrite('~/Downloads/outra-floresta.png', imagem)

cv2.destroyAllWindows()

# Fim abrir uma imagem
