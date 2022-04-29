# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Cria um arranjo de 0 até 9 dividido em 10 partes iguais
x = np.linspace(0, 9, 10)  

# Equação da reta
y = 2 * x + 1

# Criamos o plot para os valores de x e y
plt.plot(x, y, "r-") #b- é cor azul
plt.show()

##################

import numpy as np
import matplotlib.pyplot as plt

# Cria um arranjo de -2 até 2 dividido em 100 partes iguais
x = np.linspace(-2, 2, 100)
# Equação de uma parábola
y = x ** 2 

# Criamos o plot para os valores de x e y
plt.plot(x, y, "r-")
plt.show()


##################


# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating vectors X and Y valores vão desde -2 a 2 dividido em 100 partes
x = np.linspace(-2, 2, 100)
y = x ** 2 # representa a potencia de Y=x^2 parabola

fig = plt.figure(figsize = (10, 5)) #cria uma figura com dimensões 10,5
# plotar os pontos
plt.plot(x, y)
# mostra o grafico
plt.show()

