lado_1 = float(input("Informe o primeiro do triângulo:"))
lado_2 = float(input("Informe o segundo lado do triângulo:"))
lado_3 = float(input("Informe o terceiro lado do triângulo:"))

if not (lado_1 + lado_2 > lado_3 and 
        lado_1 + lado_3 > lado_2 and 
        lado_2 + lado_3 > lado_1):

    print("Isso não é um triângulo")

elif lado_1 == lado_2 == lado_3:
    print("Isso é um Triângulo Equilátero , PARABÉNS !!!")

elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print("Isso é um Triângulo Isósceles , PARABÉNS !!!")

else:
    print("Isso é um Triângulo Escaleno , PARABÉNS !!!")
