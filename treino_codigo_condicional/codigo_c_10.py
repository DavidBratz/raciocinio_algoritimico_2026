print("Digite M para Turno Matutino ou V para Turno vespertino ou 3 para turno Noturno")
turno = input("Informe em qual turno você estuda:")

if turno == "m":
    print("Bom dia!, Você estuda de manhã parabéns!")
elif turno == "v":
    print("Bom dia!, Você estuda de tarde parabéns!")
elif turno == "n":
    print("Bom dia!, Você estuda de noite parabéns!")
else:
    print("Essa opção é inválida , tente novamente!")
