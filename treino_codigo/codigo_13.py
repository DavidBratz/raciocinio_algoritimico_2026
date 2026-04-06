altura = float(input("INSIRA A SUA ALTURA:"))
print("DIGITE 1 SE FOR HOMEM OU 2 SE FOR MULHER:")
sexo = int(input("DIGITE O SEU SEXO"))
if sexo == 1:
    peso_ideal_h = (altura * 72.7) - 58
    print(f"SUA ALTURA IDEAL É DE:{peso_ideal_h:.2f}")
else:
    peso_ideal_m = (62.1 * altura) - 44.7
    print(f"SUA ALTURA IDEAL É DE:{peso_ideal_m:.2f}")
