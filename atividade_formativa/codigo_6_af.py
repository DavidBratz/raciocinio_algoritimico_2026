#----------------------- FATORIAL DE UM NÚMERO ------------------------------------------------
numero = int(input("DIGITE UM NÚMERO INTEIRO POSITIVO: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial = fatorial * i

print(f"O FATORIAL DE {numero} É: {fatorial}")
