quantidade = int(input("Digite a quantidade de alunos da disciplina:"))

abaixo_media = 0
na_media = 0
acima_media = 0
for i in range(quantidade):
    nota = int(input(f"Informe a nota do {1 + i}º aluno:"))
    if nota < 60:
        abaixo_media += 1
    elif nota > 60:
        acima_media +=1
    else:
        na_media += 1
print(f"A quantidade de alunos acima da média é: {acima_media}")
print(f"A quantidade de alunos na média é: {na_media}")
print(f"A quantidade de alunos abaixo da média é: {abaixo_media}")
