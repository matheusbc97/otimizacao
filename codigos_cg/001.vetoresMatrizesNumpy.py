# -*- coding: utf-8 -*-
# Carrega biblioteca
import numpy as np

# Cria uma matriz
matrix = np.array([[1, 4],
                    [2, 5]])

print(matrix)
# Retorna a determinante da matriz
np.linalg.det(matrix)

# Retorna a diagonal
matrix.diagonal()

# Calcula a inversa
np.linalg.inv(matrix)

# Multiplica a matriz por sua inversa
matrix @ np.linalg.inv(matrix)


#########

# Cria dois vectores
vector_a = np.array([1,2,3])
vector_b = np.array([4,5,6])

# calcula o produto interno
np.dot(vector_a, vector_b)

# calcula o produto interno (Python 3.5+)
vector_a @ vector_b

# Cria uma matriz
matrix_a = np.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 2]])

# Cria uma matriz
matrix_b = np.array([[1, 3, 1],
                    [1, 3, 1],
                    [1, 3, 8]])

# Soma duas matrizes
np.add(matrix_a, matrix_b)

# Subtrai dias matrizes
np.subtract(matrix_a, matrix_b)

# Outra forma de somar e subtrair matrizes
matrix_a + matrix_b

# Multiplica duas matrizes
np.dot(matrix_a, matrix_b)

# Multiplica duas matrizes (outra forma)
matrix_a @ matrix_b


