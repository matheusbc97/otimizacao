import cv2
from cv2 import cvtColor
import os
from matplotlib import pyplot as plt
import numpy as np

imagem = cv2.imread(os.path.expanduser( "~/Downloads/floresta.png"))

def loadImage():
    cv2.imshow('Image', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Carregamento de imagem feito com sucesso!\n")
    showOptions()

def convertImageColor(conversionType):
    if(conversionType == 'grey'):
        gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray", gray)
    elif(conversionType == 'hsv'):
        hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv", hsv)
    elif(conversionType == 'hls'):
        hls = cv2.cvtColor(imagem, cv2.COLOR_BGR2HLS)
        cv2.imshow("hls", hls)
    elif(conversionType == 'YCrCB'):
        YCrCB = cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
        cv2.imshow("YCrCB", YCrCB)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Conversão feita com sucesso!\n")
    showOptions()

def showImageColorsConvertionsOptions():
    print("Escolha uma das opção abaixo de conversão:")
    print("[1] - Tons de cinza")
    print("[2] - HSV")
    print("[3] - HSL")
    print("[4] - YCrCB")
    opcao = input()

    if (opcao == "1"):
        convertImageColor('grey')
    elif (opcao == "2"):
        convertImageColor('hsv')
    elif (opcao == "3"):
        convertImageColor('hls')
    elif (opcao == "4"):
        convertImageColor('YCrCB')

def showHistogram(histogramType):
    plt.figure()
  
    plt.xlabel("Itensidade")
    plt.ylabel("Número de pixels")

    if (histogramType == 'mono'):
        imagemCinza = cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        histograma = cv2.calcHist([imagemCinza], [0], None, [256], [0,256])
        plt.title("Histograma Monocromático")
        plt.plot(histograma)
        plt.xlim([0, 256])

    elif (histogramType == 'rgb'):
        channel = cv2.split(imagem)
        cores = ("b", "g", "r")

        for (canal, cor) in zip(channel, cores):
            histogramaRGB = cv2.calcHist([canal], [0], None, [256], [0,256])
            plt.plot(histogramaRGB, color=cor)
            plt.xlim([0, 256])

    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    showOptions()

def showHistogramsOptions():
    print("Escolha um dos histograms abaixo:")
    print("[1] - Histograma da imagem monocromática")
    print("[2] - Histograma da imagem original RGB")
    opcao = input()

    if (opcao == "1"):
        showHistogram('mono')
    elif (opcao == "2"):
        showHistogram('rgb')

def highlightByHistogram():
    # Converte imagem para tons de cinza
    imagem2 = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

    # Realce da imagem usando equalização de histogramas
    imagemEq = cv2.equalizeHist(imagem2)

    # Empilha imagens lado a lado
    resultado = np.hstack((imagem2, imagemEq))

    #Mostra resultados
    cv2.imshow('Imagem original - imagem equalizada',resultado)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    showOptions()

def showFiltersOptions():
    print("Escolha um dos histograms abaixo:")
    print("[1] - Média")
    print("[2] - Mediana")
    #print("[3] - Sobel")
    print("[4] - Gaussiano")
    #print("[5] - Laplaciano")
    opcao = input()

    if (opcao == "1"):
        media = np.hstack([
            cv2.blur(imagem,(3,3)),
            cv2.blur(imagem,(5,5)),
            cv2.blur(imagem,(7,7))
        ])
        cv2.imshow('Filtro média',media)
        cv2.waitKey(0)
    elif (opcao == "2"):
        # filtro mediana com diferentes máscaras
        # Empilha resultados lado a lado
        mediana = np.hstack([
            cv2.medianBlur(imagem,3),
            cv2.medianBlur(imagem,5),
            cv2.medianBlur(imagem,7)
        ])

        cv2.imshow('Filtro mediana',mediana)
        cv2.waitKey(0)
    elif (opcao == "4"):
        # filtro gaussiano com diferentes máscaras
        # Empilha resultados lado a lado
        gauss= np.hstack([
        cv2.GaussianBlur(imagem,(3,3),0),
        cv2.GaussianBlur(imagem,(5,5),0),
        cv2.GaussianBlur(imagem,(7,7),0)])

        cv2.imshow('Filtro gaussiano',gauss)
        cv2.waitKey(0)
    showOptions()


def showOptions():
    print("Escolha uma das perações abaixo:")
    print("[1] - Carregar uma imagem")
    print("[2] - Binarizar uma imagem")
    print("[3] - Conversão da imagem para outro sistema de cor")
    print("[4] - Mostrar o histograma da imagem")
    print("[5] - Realce da imagem por meio de equalização de histogramas")
    print("[6] - Aplicar filtros")
    print("[7] - Detectar bordas com o método de Canny")
    print("[8] - Salvar a imagem processada em um novo arquivo")
    print("[9] - Sair da aplicação")
    opcao = input()
    
    if (opcao == "1"):
        loadImage()
    elif (opcao == "3"):
        showImageColorsConvertionsOptions()
    elif (opcao == "4"):
        showHistogramsOptions()
    elif (opcao == "5"):
        highlightByHistogram()
    elif (opcao == "6"):
        showFiltersOptions()
        


showOptions()