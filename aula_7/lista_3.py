a = []
for i in range(10):
    numero = int(input(f"Digite o {1 + i}º número inteiro:"))
    a.append(numero)
maior = max(a)
menor = min(a)
print(f"O maior número é o número {maior}")
print(f"O menor número é o número {menor}")
