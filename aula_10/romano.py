romano = input("Digite o número romano: ").upper()

dicionario = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
total = 0

for i in range(len(romano)):
    if i < len(romano)-1 and dicionario[romano[i]] < dicionario[romano[i+1]]:
        total = total - dicionario[romano[i]]
    else:
        total = total + dicionario[romano[i]]
print(total)
