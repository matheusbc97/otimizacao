import matplotlib.pyplot as plt

figure, axes = plt.subplots()

# Desenha um círculo com centro (5,3) e radio=2
circulo = plt.Circle((5, 3), 2)

# Define limites do eixos xy
axes.set_aspect(1) #serve para q o circulo mantenha a proporção
axes.set_xlim(0,10) # define limites eixo x
axes.set_ylim(0,10) # define limites eixo y

# Adiciona e mostra circulo ao sistema de coordenadas.
axes.add_artist(circulo)
plt.title('Circulo')
plt.show()

#########

import matplotlib.pyplot as plt

figure, axes = plt.subplots()

# Desenha um círculo com centro (5,3) e radio=2
circulo = plt.Circle((5, 3), 2, fill=False, color='y')

# Define limites do eixos xy
axes.set_aspect(1)
axes.set_xlim(0,10)
axes.set_ylim(0,10)

# Adiciona e mostra circulo ao sistema de coordenadas.
axes.add_artist(circulo)
plt.title('Circulo')
plt.show()


#########


import numpy as np
import matplotlib.pyplot as plt

# teta varia de 0 a 2*pi
# desenhar circulo usando coordenadas polares
theta = np.linspace(0, 2*np.pi, 100)

radio = 0.3
x = radio*np.cos(theta)
y = radio*np.sin(theta)

figure, axes = plt.subplots(1)

# Criamos o plot
axes.plot(x, y)
axes.set_aspect(1)

plt.title('Círculo usando a equação paramétrica')
plt.show()

