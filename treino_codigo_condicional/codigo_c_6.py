num1 = float(input("INFORME O PRIMEIRO NÚMERO:"))
num2 = float(input("INFORME O SEGUNDO NÚMERO:"))
num3 = float(input("INFORME O TERCEIRO NÚMERO:"))

if num1 == num2 and num2 ==num3:
    print("TODOS OS NÚMEROS QUE VOCÊ DIGITOU SÃO IGUAIS")
elif num1 >= num2 and num1 >= num3:
    print(f"O MAIOR NÚMERO ENTRE ESSES QUE VOCÊ DIGITOU É O: {num1} ")
elif num2 >= num1 and num2 >= num3:
    print(f"O MAIOR NÚMERO ENTRE ESSES QUE VOCÊ DIGITOU É O: {num2} ")
else:
    print(f"O MAIOR NÚMERO ENTRE ESSES QUE VOCÊ DIGITOU É O: {num3} ")
