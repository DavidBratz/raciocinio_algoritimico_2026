valor_a = float(input("Informe o valor de A"))

if valor_a == 0:
    print("Isso não é uma equação de segundo grau")
else:

    valor_b = float(input("Informe o valor de B"))
    valor_c = float(input("Informe o valor de C"))
    delta = valor_b**2 - (4 * valor_a * valor_c)
    if delta < 0:
        print("Essa equação não possui raízes reais")
    elif delta == 0:
        valor_x = -valor_b / (2*valor_a)
        print(f"Essa equação só possui uma raiz que é:{valor_x:.2f}")
    else:
        valor_x1 = (-valor_b + (delta**0.5)) / (2 * valor_a)
        valor_x2 = (-valor_b - (delta**0.5)) / (2 * valor_a)
        print(f"Essa equação possui duas raízes reais que são elas: {valor_x1} e {valor_x2}")
