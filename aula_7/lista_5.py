numeros = []

for i in range(5):
    numero = int(input(f"Informe o {1+i}º número:"))
    numeros.append(numero)

pares = [num for num in numeros if num % 2 == 0 ]
impares = [num for num in numeros if num % 2 != 0 ]
if pares:
    print(f"O maior número par nessa lista é o número:{max(pares)}")
else:
    print("Não há números pares nessa lista")
if impares:
    print(f"O menor número ímpar nessa lista é o número:{min(impares)}")
else:
    print("Não há números ímpares nessa lista")
soma = sum(numeros)
media = soma / len(numeros)

print(f"A soma dos números dessa lista é:{soma}")
print(f"A média dos números dessa lista é:{media:.2f}")
