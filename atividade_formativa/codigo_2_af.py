#----------------------- SOMA DOS NUMEROS PARES ------------------------------------------------

#----------------------- VARIAVEIS -------------------------------------------------------------
limite = int(input("DIGITE UM NÚMERO INTEIRO POSITIVO: "))
contador = 0
soma = 0
#------------------------------- CONTAS --------------------------------------------------------
while contador <= limite:
    if contador % 2 == 0:
        soma = soma + contador
    contador += 1
#---------------------------------- SAIDA ------------------------------------------------------
print(f"A SOMA DOS NÚMEROS PARES ATÉ {limite} É: {soma}")
