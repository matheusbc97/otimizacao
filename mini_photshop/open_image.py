import cv2
import os
# Abrir imagem
imagem = cv2.imread(os.path.expanduser( "~/Downloads/floresta.png"))

cv2.imshow('Image', imagem)

print("Altura: {} pixels".format(imagem.shape[0]))
print("Largura: {} pixels".format(imagem.shape[1]))
print("Canais: {} pixels".format(imagem.shape[2]))

cv2.imwrite('./outra-floresta.png', imagem)

cv2.waitKey()

cv2.destroyAllWindows()

# Fim abrir uma imagem
