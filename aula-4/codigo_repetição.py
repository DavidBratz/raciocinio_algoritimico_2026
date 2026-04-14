#------------VARIAVEIS----------------------------------------------------------------------------------------
media_turma = 0
soma_das_notas = 0
quantidade_alunos = 0 
nota = 1.0
#------------------ CONTA DAS NOTAS (UTILIZANDO WHILE)--------------------------------------------------------
while nota > 0.0:
    nota = float(input(f"DIGITE A NOTA DO ALUNO : {quantidade_alunos}, DIGITE VALOR NEGATIVO PARA ENCERRAR:"))
    if nota < 0.0:
        break
    soma_das_notas += nota    
    quantidade_alunos += 1
media_turma = soma_das_notas/quantidade_alunos
print("A MÉDIA DA TURMA FOI:", media_turma) 

