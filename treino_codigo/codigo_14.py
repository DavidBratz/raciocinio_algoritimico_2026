peso = float(input("DIGITE O PESO DOS PEIXES EM Kg:"))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"VOCÊ TEM UM EXCESSO DE PEIXES DE:{excesso: .2f}Kg")
    print(f"O VALOR DA MULTA QUE DEVERÁ PAGAR É DE R$:{multa: .2f}")
else:
    excesso = 0 
    multa = 0 
    print("VOCÊ ESTÁ DENTRO DO LIMITE DE Kg")
    print(f"EXCESSO DE PEIXES DE: {excesso: .2f} Kg")
    print(f"MULTA DE R$ {multa: .2f}")
