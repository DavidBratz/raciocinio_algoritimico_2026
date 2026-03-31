num1 = float(input("digite o primeiro numero :  "))
num2 = float(input("digite o segundo numero :"))

opcao = str(input("informe a operacao:"))
if opcao == "soma":
    soma = num1 + num2
    print("a soma é:", soma)

elif opcao == "divisao":
    divisao = num1 / num2
    print("a divisao é:", divisao)

elif  opcao == "multiplicacao":
    multiplicacao = num1 * num2
    print("a multiplicacao é :",  multiplicacao)

elif opcao == ("subtracao"):
    subtracao = num1 - num2
    print("a subtracao é:", subtracao)
else:
    print("informe entre as opcoes : soma , divisao , multiplicacao e subtracao")