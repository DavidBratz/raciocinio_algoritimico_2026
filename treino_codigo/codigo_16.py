import math
print("SEJA BEM VINDO À NOSSA LOJA")
print("CADA LATA NOSSA TEM 18 LITROS DE TINTA")
print("1 LITRO DE TINTA EQUIVALE A 3M² DE ÁREA PINTADA")
print("CADA LATA DE TINTA CUSTA 80R$")
tamanho = float(input("INFORME O TAMANHO DA ÁREA QUE DESEJA PINTAR EM M²:"))
litro_necessario = tamanho / 3 
print(f"PARA PINTAR ESSA ÁREA VOCÊ PRECISA DE {litro_necessario:.2f} LITROS DE TINTA")
latas = math.ceil(litro_necessario / 18)
print(f"ENTÃO SERÃO NECESSÁRIAS {latas:} LATAS DE TINTA")
preço_pagar = 80 * latas
print(f"PARA PINTAR ESSA ÁREA VOCÊ VAI PAGAR CERCA DE R${preço_pagar:.2f}")
