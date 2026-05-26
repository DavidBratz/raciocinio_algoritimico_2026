import numpy as np

# Definindo quantidade de linhas e colunas
m = 3
n = 3

# Inicializando uma matriz vazia
matriz = []

# Preenchendo a matriz com a lei i * j + 1
for i in range(m):
    linha = []

    for j in range(n):
        elemento = i * j + 1
        linha.append(elemento)

    matriz.append(linha)

# Convertendo para matriz NumPy
matriz_np = np.array(matriz)

# Exibindo resultado
print(matriz_np)
