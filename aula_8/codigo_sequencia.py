quantidade_num = int(input("Informe a quantidade de números que deseja:"))
seq_num = []

for i in range(quantidade_num):
    numeros = float(input(f"Informe {1 + i}º número:"))
    seq_num.append(numeros)
print(f"Os números da lista são: {seq_num}")

maior_seq = 1
quant_v_c = 1
numero_seq = seq_num[0]

for i in range (1, len(seq_num)):
    if seq_num [i] == seq_num [i - 1]:
        quant_v_c = quant_v_c + 1 
    else:
        quant_v_c = 1

    if quant_v_c > maior_seq:
        maior_seq = quant_v_c
        numero_seq = seq_num[i]
        
print(f"A maior sequencia de números iguais consecutivos na lista foi , o número {numero_seq} se repetindo {maior_seq} vezes consecutivas.")
