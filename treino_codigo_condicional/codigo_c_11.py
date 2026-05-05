salario_inc = float(input("Informe o seu salário atual: "))
salario = 0

if salario_inc <= 280:
   percentual = 0.2
elif salario_inc > 280 and salario_inc <= 700:
   percentual = 0.15
elif salario_inc > 700 and salario_inc <= 1500:
   percentual = 0.1
else:
   percentual = 0.05

salario_antigo = salario_inc
aumento = salario_inc * percentual
salario = salario_inc + aumento

print(f"SALÁRIO ANTES DO REAJUSTE: R$ {salario_antigo}")
print(f"PERCENTUAL DE AUMENTO APLICADO: {percentual * 100}%")
print(f"VALOR DO AUMENTO: R$ {aumento}")
print(f"NOVO SALÁRIO: R$ {salario}")
