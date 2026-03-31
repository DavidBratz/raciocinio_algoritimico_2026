avaliacao_final = 0.0 
media = 6.0
while(True):
    avaliacao_1 = float(input("INFORME SUA NOTA DA AVALIAÇÃO 1:"))
    if(avaliacao_1 < 0.0 or avaliacao_1 > 5.0):
        print("VALOR INVÁLIDO , MAIOR  NOTA POSSÍVEL É 5")
    else:
        break
while(True):
    avaliacao_2 = float(input("INFORME SUA NOTA DA AVALIAÇÃO 2:"))
    if(avaliacao_2 < 0.0 or avaliacao_2 > 5.0):
        print("VALOR INVÁLIDO , MAIOR NOTA POSSÍVEL É 5")
    else:
        break
    
if (avaliacao_1 + avaliacao_2) >= media:
    print("VOCÊ ESTÁ APROVADO")
    print("PARABÉNS")

elif (avaliacao_1 < 1 and avaliacao_2 < 1):
    print("VOCÊ REPROVOU")
    print("SINTO MUITO")
else:
    print("VOCÊ PRECISA FAZER PROVA FINAL")

    avaliacao_final = float(input("INFORME SUA NOTA DA AVALIAÇÃO FINAL:"))

    if ((avaliacao_final + avaliacao_1) >= media):
        print("VOCÊ ESTÁ APROVADO,APÓS PROVA FINAL")
    elif((avaliacao_final + avaliacao_2) >= media):
        print("VOCÊ ESTÁ APROVADO,APÓS PROVA FINAL")
    elif((avaliacao_final + avaliacao_1) < media):
        print("VOCÊ ESTÁ REPROVADO,APÓS PROVA FINAL")
    else:
        print("VOCÊ ESTÁ REPROVADO,APÓS PROVA FINAL")
