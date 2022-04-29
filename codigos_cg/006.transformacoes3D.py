#Profa. Edhelmira Lima;
#Data: 26-10-2021
#Exemplo: Código base para transformação geométrica de poliedros

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# Preparamos uma figura no espaço 3D
fig = plt.figure(1)
ax = fig.gca(projection='3d')

# Sejam os pontos do poliedro
P1= (0,0,0)
P2= (0,0,-4)
P3= (2,0,0)
P4= (2,0,-4)
P5= (1,-1,0)
P6= (1,-1,-4)
P7= (0,-2,0)
P8= (2,-2,0)
P9= (0,-2,-4)
P10= (2,-2,-4)

# Desenhamos os pontos
ax.scatter(P1[0],P1[1],P1[2], c='b')
ax.scatter(P2[0],P2[1],P2[2], c='b')
ax.scatter(P3[0],P3[1],P3[2], c='b')
ax.scatter(P4[0],P4[1],P4[2], c='b')
ax.scatter(P5[0],P5[1],P5[2], c='b')
ax.scatter(P6[0],P6[1],P6[2], c='b')
ax.scatter(P7[0],P7[1],P7[2], c='b')
ax.scatter(P8[0],P8[1],P8[2], c='b')
ax.scatter(P9[0],P9[1],P9[2], c='b')
ax.scatter(P10[0],P10[1],P10[2], c='b')

# Criamos os rótulos dos pontos
ax.text(P1[0],P1[1],P1[2], 'P1', size=12, zorder=1, color='k')
ax.text(P2[0],P2[1],P2[2], 'P2', size=12, zorder=1, color='k')
ax.text(P3[0],P3[1],P3[2], 'P3', size=12, zorder=1, color='k')
ax.text(P4[0],P4[1],P4[2], 'P4', size=12, zorder=1, color='k')
ax.text(P5[0],P5[1],P5[2], 'P5', size=12, zorder=1, color='k')
ax.text(P6[0],P6[1],P6[2], 'P6', size=12, zorder=1, color='k')
ax.text(P7[0],P7[1],P7[2], 'P7', size=12, zorder=1, color='k')
ax.text(P8[0],P8[1],P8[2], 'P8', size=12, zorder=1, color='k')
ax.text(P9[0],P9[1],P9[2], 'P9', size=12, zorder=1, color='k')
ax.text(P10[0],P10[1],P10[2], 'P10', size=12, zorder=1, color='k')

# Criamos as arestas entre dois pontos
ax.plot([P1[0],P2[0]], [P1[1],P2[1]], [P1[2],P2[2]], c='r') #p1-p2
ax.plot([P1[0],P3[0]], [P1[1],P3[1]], [P1[2],P3[2]], c='r') #p1-p3
ax.plot([P1[0],P5[0]], [P1[1],P5[1]], [P1[2],P5[2]], c='r') #p1-p5
ax.plot([P2[0],P4[0]], [P2[1],P4[1]], [P2[2],P4[2]], c='r') #p2-p4
ax.plot([P2[0],P6[0]], [P2[1],P6[1]], [P2[2],P6[2]], c='r') #p2-p6
ax.plot([P3[0],P4[0]], [P3[1],P4[1]], [P3[2],P4[2]], c='r') #p3-p4
ax.plot([P3[0],P5[0]], [P3[1],P5[1]], [P3[2],P5[2]], c='r') #p3-p5
ax.plot([P4[0],P6[0]], [P4[1],P6[1]], [P4[2],P6[2]], c='r') #p4-p6
ax.plot([P5[0],P6[0]], [P5[1],P6[1]], [P5[2],P6[2]], c='r') #p5-p6
ax.plot([P5[0],P7[0]], [P5[1],P7[1]], [P5[2],P7[2]], c='r') #p5-p7
ax.plot([P5[0],P8[0]], [P5[1],P8[1]], [P5[2],P8[2]], c='r') #p5-p8
ax.plot([P6[0],P9[0]], [P6[1],P9[1]], [P6[2],P9[2]], c='r') #p6-p9
ax.plot([P6[0],P10[0]], [P6[1],P10[1]], [P6[2],P10[2]], c='r') #p6-p10
ax.plot([P7[0],P8[0]], [P7[1],P8[1]], [P7[2],P8[2]], c='r') #p7-p8
ax.plot([P7[0],P9[0]], [P7[1],P9[1]], [P7[2],P9[2]], c='r') #p7-p9
ax.plot([P8[0],P10[0]], [P8[1],P10[1]], [P8[2],P10[2]], c='r') #p8-p10
ax.plot([P9[0],P10[0]], [P9[1],P10[1]], [P9[2],P10[2]], c='r') #p9-p10

# Mostramos a figura
plt.show()
