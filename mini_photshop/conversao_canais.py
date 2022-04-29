import cv2
import os

# Abrir imagem
imagem = cv2.imread(os.path.expanduser( "~/Downloads/floresta.png"))
cv2.imshow('Image', imagem)

gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)

hls = cv2.cvtColor(imagem, cv2.COLOR_BGR2HLS)
cv2.imshow("hls", hls)

YCrCB = cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
cv2.imshow("YCrCB", YCrCB)

luv = cv2.cvtColor(imagem, cv2.COLOR_BGR2LUV)
cv2.imshow("luv", luv)

lab = cv2.cvtColor(imagem, cv2.COLOR_BGR2LAB)
cv2.imshow("lab", lab)

cv2.waitKey(0)
cv2.destroyAllWindows()