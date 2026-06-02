a = []
b = []
c = []

for i in range(10):
    num_a = int(input(f"Insira o {i + 1}ª Número para o vetor A:"))
    a.append(num_a)

for i in range(10):
    num_b = int(input(f"Insira o {i + 1}ª Número para o vetor B:"))
    b.append(num_b)

for i in range(10):
    c.append(a[i])
    c.append(b[i])

print(f"O vetor intercalado é: {c}")
