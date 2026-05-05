n = 0

while n <= 0:
    n = int(input("Informe o valor de n (maior que 0): "))

linhas = 0

while linhas< n:
    coluna = 0
    linha = ""

    while coluna < n:
        linha += "X "
        coluna += 1

    print(linha)
    linhas += 1
