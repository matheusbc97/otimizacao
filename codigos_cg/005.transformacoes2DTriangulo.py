import numpy as np # para manipulação de matrizes
from matplotlib import pyplot as plt # para plotar dados

# criamos as matrizes de transformção
def translacao2D(dx, dy):
    return np.array([[1,0,dx],
                     [0,1,dy],
                     [0,0,1]])

def escala2D(sx, sy):
    return np.array([[sx,0,0],
                     [0,sy,0],
                     [0,0,1]])

def rotacao2D(tetha):
    tetha = tetha*np.pi/180
    return np.array([[np.cos(tetha),-np.sin(tetha),0],
                     [np.sin(tetha),np.cos(tetha),0],
                     [0,0,1]])

# função que desenha um polígono dado uma lista de pontos X
def desenhaTriangulo(X, cor):
    plt.subplots(figsize=(6, 6)) #tamanho figura 6x6 polegadas
    plt.scatter(X[:, 0], X[:, 1], s=10, color=cor)
    t1 = plt.Polygon(X[:3, :2], color=cor)
    plt.gca().add_patch(t1)
    plt.xlim([-10, 15])
    plt.ylim([-10, 15])
    plt.show()

########
# Pontos de um triângulo em coordenadas homogêneas
p1 = np.array([[3],[2],[1]])
p2 = np.array([[9],[2],[1]])
p3 = np.array([[7],[10],[1]])
#p = [6, 5]
p = np.array([[6],[5],[1]]) # eixo de rotação

# plotar triângulo original
X = np.array([p1.transpose()[0],p2.transpose()[0],p3.transpose()[0]])
desenhaTriangulo(X,'red')

#---------------------------------------------------------
#Rotar 90 graus p
#t = rotacao2D(90) # teste sem composição de transformações
#t = translacao2D(2,1)
#t = escala2D(0.5,0.3)
# calcular matriz de rotação sobre o eixo
t = (translacao2D(p[0],p[1]) @ rotacao2D(90)) @ translacao2D(-p[0],-p[1])
p1 = t @ p1
p2 = t @ p2
p3 = t @ p3

# Plotar triangulo após rotação
X = np.array([p1.transpose()[0],p2.transpose()[0],p3.transpose()[0]])
desenhaTriangulo(X,'blue')
