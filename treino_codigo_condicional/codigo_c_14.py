nota_1 = float(input("Informe a nota do aluno no semestre:"))
nota_2 = float(input("Informe a nota do aluno no semestre:"))

media = (nota_1 + nota_2) / 2

if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

print(f"As notas do aluno foram {nota_1}/10 e {nota_2}/10")
print(f"A média do aluno foi de {media:.2f}/10")
print(f"O Conceito que o aluno obteve foi {conceito}")

if conceito == "A" or conceito =="B" or conceito =="C":
    print("O aluno foi aprovado")
else:
    print("O aluno foi reprovado")
