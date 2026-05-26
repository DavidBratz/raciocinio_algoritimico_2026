import numpy as np

matriz = np.array([[0,1,2],
                   [3,4,5],
                   [6,7,8],
                   [9,0,0]
])

#---------------- Matriz transposta ------------------
print(matriz.T)

#---------------- Soma dos números da matriz ---------
soma = matriz + matriz
print(soma)

#--------------- Linhas da matriz --------------------
for linha in matriz:
    print(soma)

#--------------- Número específico da matriz ---------
print("O item nessa coluna e linha é =",[matriz[0][0]])
