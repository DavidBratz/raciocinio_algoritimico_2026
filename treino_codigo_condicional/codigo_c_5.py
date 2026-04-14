num1 = float(input("INFORME SUA PRIMEIRA NOTA:"))
num2 = float(input("INFORME SUA SEGUNDA NOTA:"))
media = (num1 + num2) / 2
if media == 10:
    print("VOCÊ ESTÁ APROVADO COM DISTINÇÃO , PARABÉNS PELA DEDICAÇÃO")
elif media >= 7:
    print("VOCÊ ESTÁ APROVADO, PARABÉNS")
else:
    print("VOCÊ ESTÁ REPROVADO , POR FAVOR MELHORE")
