print("Valor mínimo para o saque é de 10R$ e o máximo é de 600R$")
valor_s = float(input("Digite o valor que deseja sacar: "))

nota_1 = 0 
nota_5 = 0 
nota_10 = 0 
nota_50 = 0 
nota_100 = 0 

while valor_s < 10 or valor_s > 600:
    print("Esse valor não pode ser sacado, digite um número válido")
    valor_s = float(input("Digite o valor que deseja sacar: "))
    
nota_100 = int(valor_s / 100)      
resto = valor_s % 100             

nota_50 = int(resto / 50)
resto = resto % 50

nota_10 = int(resto / 10)
resto = resto % 10

nota_5 = int(resto / 5)
resto = resto % 5

nota_1 = int(resto)

print(f" O valor sacado: R$ {valor_s:.2f}")
if nota_100 > 0:
    print(f"{nota_100}x R$ 100,00")
if nota_50 > 0:
    print(f"{nota_50}x R$  50,00")
if nota_10 > 0:
    print(f"{nota_10}x R$  10,00")
if nota_5 > 0:
    print(f"{nota_5}x R$   5,00")
if nota_1 > 0:
    print(f"{nota_1}x R$    1,00")
