import numpy as np

def validar(mapa,x,y,navio,h):
    if h == 1:  # horizontal
        if y + navio > 10:
            return False
        for i in range(y, navio + y):
            if mapa[x][i] != 0:
                return False
    else:  # vertical
        if x + navio > 10:
            return False
        for i in range(x, navio + x):
            if mapa[i][y] != 0:
                return False
    return True

def distribuir_navios(mapa):
    navios = [5,4,4,3,3,3,2,2]
    
    for navio in navios:
        while True:
            mostrar_mapa(mapa)

            x = int(input("Digite o valor desejado para coordenado no navio no eixo X: "))
            y = int(input("Digite o valor desejado para coordenado no navio no eixo Y: "))
            h = int(input("Digite 1 para HORIZONTAL ou 2 para VERTICAL: "))

            if validar(mapa,x,y,navio,h):
                if h == 1:
                    for i in range(y, navio + y):
                        mapa[x][i] = navio
                else:
                    for i in range(x, navio + x):
                        mapa[i][y] = navio
                break
            else:
                print("Não pode colocar o navio aí!")

def atacar(mapa_atacante,mapa_defensor):

    x = int(input("Digite o eixo X desejado: "))
    y = int(input("Digite o eixo Y desejado: "))

    if mapa_defensor[x][y] == 0:
        print("Acertou a Água")
        mapa_atacante[x][y] = -1
    else:
        mapa_atacante[x][y] = mapa_defensor[x][y]
        mapa_defensor[x][y] = 0
        print(f"Você acertou um navio de tamanho: {mapa_atacante[x][y]}")

def vencedor(mapa):

    for linha in mapa:
        for valor in linha:
            if valor > 0:
                return False
    return True

def criar_mapa():
    return np.zeros((10,10))

def mostrar_mapa(mapa):
    print(mapa)

mapa_j1 = criar_mapa()
mapa_j2 = criar_mapa()
mapa_atk_j1 = criar_mapa()
mapa_atk_j2 = criar_mapa()

print("Jogador 1 - Posicione seus navios")
distribuir_navios(mapa_j1)

print("Jogador 2 - Posicione seus navios")
distribuir_navios(mapa_j2)

while True:

    print("Turno Jogador 1")
    mostrar_mapa(mapa_atk_j1)
    atacar(mapa_atk_j1,mapa_j2)

    if vencedor(mapa_j2):
        print("Jogador 1 venceu!")
        break

    print("Turno Jogador 2")
    mostrar_mapa(mapa_atk_j2)
    atacar(mapa_atk_j2,mapa_j1)

    if vencedor(mapa_j1):
        print("Jogador 2 venceu!")
        break
