import cv2
from cv2 import cvtColor
import os
from matplotlib import pyplot as plt
import numpy as np

def loadImage():
    imagem = cv2.imread(os.path.expanduser( "~/Downloads/projeto/lena.png"))
    cv2.imshow('Image', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Carregamento de imagem feito com sucesso!\n")
    showOptions(imagem)

def convertImageColor(conversionType, imagem):
    if(conversionType == 'grey'):
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray", imagem)
    elif(conversionType == 'hsv'):
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv", imagem)
    elif(conversionType == 'hls'):
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HLS)
        cv2.imshow("hls", imagem)
    elif(conversionType == 'YCrCB'):
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
        cv2.imshow("YCrCB", imagem)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Conversão feita com sucesso!\n")
    showOptions(imagem)

def showImageColorsConvertionsOptions(imagem):
    print("Escolha uma das opção abaixo de conversão:")
    print("[1] - Tons de cinza")
    print("[2] - HSV")
    print("[3] - HSL")
    print("[4] - YCrCB")
    opcao = input()

    if (opcao == "1"):
        convertImageColor('grey', imagem)
    elif (opcao == "2"):
        convertImageColor('hsv', imagem)
    elif (opcao == "3"):
        convertImageColor('hls', imagem)
    elif (opcao == "4"):
        convertImageColor('YCrCB', imagem)

def showHistogram(histogramType, imagem):
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
    showOptions(imagem)

def showHistogramsOptions(imagem):
    print("Escolha um dos histograms abaixo:")
    print("[1] - Histograma da imagem monocromática")
    print("[2] - Histograma da imagem original RGB")
    opcao = input()

    if (opcao == "1"):
        showHistogram('mono',imagem)
    elif (opcao == "2"):
        showHistogram('rgb', imagem)

def highlightByHistogram(imagem):
    # Converte imagem para tons de cinza
    imagem = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

    # Realce da imagem usando equalização de histogramas
    imagemEq = cv2.equalizeHist(imagem)

    # Empilha imagens lado a lado
    imagem = np.hstack((imagem, imagemEq))

    #Mostra resultados
    cv2.imshow('Imagem original - imagem equalizada',imagem)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    showOptions(imagem)

def showFiltersOptions(imagem):
    print("Escolha um dos histograms abaixo:")
    print("[1] - Média")
    print("[2] - Mediana")
    #print("[3] - Sobel")
    print("[4] - Gaussiano")
    #print("[5] - Laplaciano")
    opcao = input()

    if (opcao == "1"):
        imagem = np.hstack([
            cv2.blur(imagem,(3,3)),
            cv2.blur(imagem,(5,5)),
            cv2.blur(imagem,(7,7))
        ])
        cv2.imshow('Filtro média',imagem)
        cv2.waitKey(0)
    elif (opcao == "2"):
        # filtro mediana com diferentes máscaras
        # Empilha resultados lado a lado
        imagem = np.hstack([
            cv2.medianBlur(imagem,3),
            cv2.medianBlur(imagem,5),
            cv2.medianBlur(imagem,7)
        ])

        cv2.imshow('Filtro mediana',imagem)
        cv2.waitKey(0)
    elif (opcao == "4"):
        # filtro gaussiano com diferentes máscaras
        # Empilha resultados lado a lado
        imagem= np.hstack([
        cv2.GaussianBlur(imagem,(3,3),0),
        cv2.GaussianBlur(imagem,(5,5),0),
        cv2.GaussianBlur(imagem,(7,7),0)])

        cv2.imshow('Filtro gaussiano',imagem)
        cv2.waitKey(0)
    showOptions(imagem)

def saveImage(imagem):
    cv2.imwrite(os.path.expanduser( "~/Downloads/projeto/outra-lena.png"), imagem)

def showOptions(imagem):
    print("Escolha uma das perações abaixo:")
    print("[1] - Carregar uma imagem")
    #print("[2] - Binarizar uma imagem")
    print("[3] - Conversão da imagem para outro sistema de cor")
    print("[4] - Mostrar o histograma da imagem")
    print("[5] - Realce da imagem por meio de equalização de histogramas")
    print("[6] - Aplicar filtros")
    #print("[7] - Detectar bordas com o método de Canny")
    print("[8] - Salvar a imagem processada em um novo arquivo")
    print("[9] - Sair da aplicação")
    opcao = input()
    
    if (opcao == "1"):
        loadImage()
    elif (opcao == "3"):
        showImageColorsConvertionsOptions(imagem)
    elif (opcao == "4"):
        showHistogramsOptions(imagem)
    elif (opcao == "5"):
        highlightByHistogram(imagem)
    elif (opcao == "6"):
        showFiltersOptions(imagem)
    elif (opcao == "8"):
        saveImage(imagem)

showOptions('')