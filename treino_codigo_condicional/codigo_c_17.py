ano = int(input("Informe o Ano que deseja descobrir:"))

if (ano % 4 == 0 and ano % 100 != 0) or ( ano % 400 == 0 ):
    print(f"Esse ano informado {ano} é bissexto")
else:
    print(f"Esse ano informado {ano} não é bissexto")
