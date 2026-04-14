#----------------------- NÚMERO PRIMO ------------------------------------------------
numero = int(input("DIGITE UM NÚMERO INTEIRO: "))
divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print(f"{numero} É UM NÚMERO PRIMO")
else:
    print(f"O NÚMERO {numero} NÃO É UM NÚMERO PRIMO")
    
