#----------------------- MÉDIA DE UMA LISTA DE NÚMEROS ------------------------------------------------
quantidade = int(input("QUANTOS NÚMEROS VOCÊ QUER DIGITAR: "))
soma = 0

for i in range(1, quantidade + 1):
    numero = float(input(f"DIGITE O {i}º NÚMERO: "))
    soma = soma + numero

media = soma / quantidade

print(f"A MÉDIA DOS NÚMEROS É: {media}")
