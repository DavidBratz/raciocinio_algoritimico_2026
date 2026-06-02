notas = []

for i in range(10):
    soma = 0
    print(f"Aluno {i+1}:")
    for j in range(4):
        nota = float(input(f"Digite a {j+1}ª nota: "))
        soma = soma + nota 

        media = soma / 4
        notas.append(media)

aprovados = 0
for media in notas:
    if media >= 7.0:
        aprovados = aprovados + 1

print(f"Número de alunos com média maior ou igual a 7.0: {aprovados}")
