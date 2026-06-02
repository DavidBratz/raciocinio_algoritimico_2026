numeros = []
soma = 0 
multiplicacao = 1

for i in range(5):
    num = int(input(f"Insira o {i + 1}ª Número:"))
    numeros.append(num)
    
    soma = soma + num
    multiplicacao = multiplicacao * num

print(f"Os números são: {numeros}")
print(f"A soma desses numeros é de: {soma}")
print(f"A multiplicação desses números é de: {multiplicacao}")
