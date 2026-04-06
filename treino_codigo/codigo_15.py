salario_hora = float(input("DIGITE SEU SÁLARIO POR HORA:"))
horas_trabalhadas = float(input("DIGITE SUAS HORAS TRABALHADAS NO MÊS:"))

salario_bruto = salario_hora * horas_trabalhadas
print(f"SEU SÁLARIO NO MÊS É DE:{salario_bruto: .2f}")

salario_ir = salario_bruto * 0.11
print(f"VOCÊ PAGOU AO IMPOSTO DE RENDA R$:{salario_ir: .2f}")

salario_inss = salario_bruto * 0.08
print(f"VOCÊ PAGOU AO INSS R$:{salario_inss: .2f}")

salario_sind = salario_bruto * 0.05
print(f"VOCÊ PAGOU AO SINDICATO R$:{salario_sind: .2f}")

salario_liquido = salario_bruto - (salario_sind + salario_inss + salario_ir)
print(f"SEU SÁLARIO LÍQUIDO É DE R$: {salario_liquido: .2f}")
