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

#criamos um ponto p1=(3,2) ....vetor coluna
p1 = np.array([[3],
               [2],
               [1]])

#translação de (dx,dy)=(4,3)
#tp1 = np.matmul(translacao2D(4,3),p1)
tp1 = translacao2D(4,3) @ p1

#escala de (sx,sy)=(2,3)
#sp1 = np.matmul(escala2D(2,3), p1)
sp1 = escala2D(2,3) @ p1

#rotação de tetha=45
#rp1 = np.matmul(rotacao2D(45),p1)
rp1 = rotacao2D(45) @ p1

#rotação no próprio eixo: transformação composta
#T=t(x,y)*R(tetha)*t(-x,-y)
#T = np.matmul(np.matmul(translacao2D(3,2),rotacao2D(45)), translacao2D(-3,-2)) são equivalentes
T = (translacao2D(3,2) @ rotacao2D(45)) @ translacao2D(-3,-2)

#rrp1 = np.matmul(T,p1)
rrp1 = T @ p1

#graficar
plt.figure()
plt.title("Pontos")
plt.xlabel("x")
plt.ylabel("y")
#plotamos os pontos
plt.scatter(p1[0],p1[1])
#plt.scatter(tp1[0],tp1[1])
#plt.scatter(sp1[0],sp1[1])
plt.scatter(rp1[0],rp1[1])

plt.xlim([-10,10])
plt.ylim([-10,10])
plt.show()
