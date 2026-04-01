ganho_hora = float(input("INFORME QUANTO VOCÊ GANHA POR HORA TRABALHADA:"))
horas_trabalhadas = float(input("INFORME QUANTAS HORAS VOCÊ TRABALHA NO MÊS:"))

salario = horas_trabalhadas * ganho_hora
print(f"SEU SALÁRIO É DE: R$ {salario:.2f}")
