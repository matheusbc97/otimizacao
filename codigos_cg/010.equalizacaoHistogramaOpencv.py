#Profa. Edhelmira Lima;
#Data: 30-11-2021
#Exemplo: Código de equalização de histogramas

import cv2
import numpy as np

# ler uma imagem de  baixo contraste
imagem = cv2.imread('lena-low.jpeg')

# Converte imagem para tons de cinza
imagem = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

# Realce da imagem usando equalização de histogramas
imagemEq = cv2.equalizeHist(imagem)

# Empilha imagens lado a lado
resultado = np.hstack((imagem, imagemEq))

#Mostra resultados
cv2.imshow('Imagem original - imagem equalizada',resultado)
cv2.waitKey(0)

cv2.destroyAllWindows()

