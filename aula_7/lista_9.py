a = []

for i in range(10):
    num = int(input(f"Insira o {i + 1}ª Número:"))
    a.append(num)

soma_quadrados = sum(x ** 2 for x in a)
print(f"A soma dos quadrados dos elementos do vetor é: {soma_quadrados}")  
