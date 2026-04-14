num1 = float(input("INFORME O PRIMEIRO NÚMERO:"))
num2 = float(input("INFORME O SEGUNDO NÚMERO:"))
num3 = float(input("INFORME O TERCEIRO NÚMERO:"))

if num1 == num2 and num2 ==num3:
    print("TODOS OS NÚMEROS QUE VOCÊ DIGITOU SÃO IGUAIS")
else:
    #------------------------- MAIOR NÚMERO ----------------------------------------
    if num1 >= num2 and num1 >= num3:
        maior = num1
    elif num2 >= num1 and num2 >= num3:
        maior = num2
    else:
        maior = num3
    #------------------------- MENOR NÚMERO ----------------------------------------
    if num1 <= num2 and num1 <= num3:
        menor = num1
    elif num2 <= num1 and num2 <= num3:
        menor = num2
    else:
        menor = num3
    #------------------------- SAÍDAS --------------------------------------------
    print(f"O MAIOR NÚMERO DENTRE ESSES QUE VOCÊ DIGITOU É: {maior}")
    print(f"O MENOR NÚMERO DENTRE ESSES QUE VOCÊ DIGITOU É: {menor}")
