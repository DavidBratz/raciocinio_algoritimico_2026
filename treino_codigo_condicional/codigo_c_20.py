nota_1 = float(input("Digite aqui a primeira nota do aluno:"))
nota_2 = float(input("Digite aqui a segunda nota do aluno:"))
nota_3 = float(input("Digite aqui a terceira nota do aluno:"))

media = ( nota_1 + nota_2 + nota_3) / 3 

if media >= 7 and media < 10:
    print(f"O aluno está aprovado com uma média de {media:.2f}/10")
elif media < 7:
    print(f"O aluno está reprovado com uma média de {media:.2f}/10")
else:
    print(f"O aluno foi aprovado com nota máxima , média de {media:.2f}/10")
