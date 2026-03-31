rendimento_mensal = float(input("INFORME SEU RENDIMENTO MENSAL:"))
numero_dependentes = int(input("INFORME O NUMERO DE DEPENDENTES:"))
pensao_alimenticia = float(input("INFORME O VALOR DA PENSAO ALIMENTICIA:"))
outras_deducoes = float(input("INFORME OUTROS VALORES:"))

valor_base = rendimento_mensal - ((numero_dependentes * 189.59) + pensao_alimenticia + outras_deducoes)
print(valor_base)

if valor_base <= 1903.98:
    faixa = "FAIXA 1"
    print("ALIQUOTA DE 0%")
    porcentagem = 0
elif valor_base <= 2826.65:
    faixa = "FAIXA 2"
    print("ALIQUOTA DE 7.5%")
    porcentagem = valor_base * 0.075
elif valor_base <= 3751.05:
    faixa = "FAIXA 3"
    print("ALIQUOTA DE 15%")
    porcentagem = valor_base * 0.15
elif valor_base <= 4664.68:
    faixa = "FAIXA 4"
    print("ALIQUOTA DE 22.5%")
    porcentagem = valor_base * 0.225
else:
    faixa = "FAIXA 5"
    print("ALIQUOTA DE 27.5%")
    porcentagem = valor_base * 0.275

print(porcentagem)
print(faixa)
