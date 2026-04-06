import math
print("\nSEJA BEM VINDO À NOSSA LOJA")
print("\nNÓS VENDEMOS TINTAS EM LATAS DE 18 LITROS OU GALÕES DE 3,6 LITROS")
print("\n1 LITRO DE TINTA EQUIVALE A 6M² DE ÁREA PINTADA")
print("\nA LATA DE TINTA CUSTA 80R$ E O GALÃO CUSTA 25R$")

tamanho = float(input("\nINFORME O TAMANHO DA ÁREA QUE DESEJA PINTAR EM M²:"))

litro_necessario = tamanho / 6 
litro_necessario = litro_necessario * 1.1
print(f"PARA PINTAR ESSA ÁREA VOCÊ PRECISA DE {litro_necessario:.2f} LITROS DE TINTA")

galoes = math.ceil(litro_necessario / 3.6)
preço_galao = galoes * 25

latas = math.ceil(litro_necessario / 18)
preço_lata = latas * 80

latas_mistura = int(litro_necessario // 18)  
resto_litros = litro_necessario - (latas_mistura * 18)
galoes_mistura = math.ceil(resto_litros / 3.6)
preço_mistura = (latas_mistura * 80) + (galoes_mistura * 25)

print("\nOpção 1: Apenas latas de 18 litros")
print(f"Latas necessárias: {latas}")
print(f"Preço total: R${preço_lata:.2f}")

print("\nOpção 2: Apenas galões de 3,6 litros")
print(f"Galões necessários: {galoes}")
print(f"Preço total: R${preço_galao:.2f}")

print("\nOpção 3: Mistura de latas e galões para menor preço")
print(f"Latas: {latas_mistura}")
print(f"Galões: {galoes_mistura}")
print(f"Preço total: R${preço_mistura:.2f}")
