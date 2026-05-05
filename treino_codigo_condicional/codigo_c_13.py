print("DIGITE 1 Para Domingo, 2 Para Segunda , 3 Para terça , 4 Para Quarta , 5 Para Quinta , 6 Para sexta ou 7 Para Sábado")
dia_s = float(input("Digite o dia da semana informando o número correspondente ao dia informado acima:"))

if dia_s == 1:
    print(f"Parabéns hoje é DOMINGO - FEIRA")
elif dia_s == 2:
    print(f"Parabéns hoje é SEGUNDA - FEIRA")
elif dia_s == 3:
    print(f"Parabéns hoje é TERÇA - FEIRA")
elif dia_s == 4:
    print(f"Parabéns hoje é QUARTA - FEIRA")
elif dia_s == 5:
    print(f"Parabéns hoje é QUINTA - FEIRA")
elif dia_s == 6:
    print(f"Parabéns hoje é SEXTA - FEIRA")
elif dia_s == 7:
    print(f"Parabéns hoje é SÁBADO - FEIRA")
else:
    print("Isso não é um número válido e muito menos um dia existente !!!")
