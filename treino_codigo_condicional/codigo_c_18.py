data = input("Informe a data no estilo dd/mm/aaaa:")

dia = int(data[0:2]) 
mes = int(data[3:5])
ano = int(data[6:10])

if mes < 1 or mes > 12:
    print("Você digitou um número de mês que não existe")
else:
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= dia <= 31:
            print("Essa data é valida")
        else:
            print("Essa data é invalida")

    elif mes in [4, 6, 9, 11]:
        if dia >= 1 and dia <= 30:
            print("Essa data é valida")
        else:
            print("Essa data é inválida")
    elif mes == 2:
        if bissexto:
            if dia >= 1 and dia <= 29:
                print("Essa data é válida")
            else:
                print("Essa data é inválida")
        else:
            if dia >= 1 and dia <= 28:
                print("Essa data é válida")
            else:
                print("Essa data é inválida")
