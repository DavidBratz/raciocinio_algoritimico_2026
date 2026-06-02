idade = []
altura = []

for i in range(5):
    edad = int(input(f"Informe a idade da {i + 1} Pessoa: "))
    idade.append(edad)

    tall = float(input(f"Informe aqui a altura da {i + 1} Pessoa: "))
    altura.append(tall)

print(f"A ordem correta das idades que vc inseriu é: {idade}")
print(f"A ordem correta das alturas que vc inseriu é: {altura}")

idade_inv = idade[::-1]
altura_inv = altura[::-1]

print(f"A ordem inversa das idades que vc inseriu é: {idade_inv}")
print(f"A ordem inversa das alturas que vc inseriu é: {altura_inv}")
