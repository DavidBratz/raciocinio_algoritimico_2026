print("ESSE É UM PROGRAMA PARA O CÁLCULO DA SUA FOLHA DE PAGAMENTO , APROVEITE E USE COM MODERAÇÃO !!!! ")

hora_t = float(input("Informe a quantidade de horas trabalhadas no mês:"))
valor_h = float(input("Informe o quanto sua hora trabalhada vale:"))
salario_b = valor_h * hora_t

if salario_b <= 900:
    ir = 0 
elif salario_b <= 1500:
    ir = salario_b * 0.05
elif salario_b <= 2500:
    ir = salario_b * 0.1
else:
    ir = salario_b * 0.2

inss = salario_b * 0.1

fgts = salario_b * 0.11

total_desc =  inss + ir 

salario_liq =salario_b - total_desc

print(f"Seu salário bruto é de: {salario_b}R$")
print(f"O desconto do imposto de renda (IR) é de: {ir}R$")
print(f"O desconto para o INSS é de : {inss}R$ ")
print(f"O desconto do seu salário para o FGTS destinado a sua empresa é de: {fgts}R$")
print(f"O total descontado do seu sálario é de: {total_desc}")
print(f"O seu salário líquido é de: {salario_liq}R$")

